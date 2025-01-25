import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.stats import norm
from numpy.linalg import norm as L2norm
from scipy.optimize import Bounds, NonlinearConstraint, differential_evolution

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, WhiteKernel

import matplotlib.pyplot as plt

class DynO:
    def __init__(self, var_names, domain, dtSampling, KXmax=[], IntegralSample=[], kernel=None, repulsion=0.1, repulsion0_decay=1.05, SamplVratio=1, no_tau_to_SS=3):
        self.var_names = var_names #variable names
        self.d = len(var_names) #domain dimensionality
        self.domain = domain #domain extension
        if not IntegralSample: self.IntegralSample = [False]*self.d #flags to indicate whether variables should be integrated
        else: self.IntegralSample = IntegralSample
        self.dtSampling = dtSampling #[min] sampling time of the in-line analysis
        if not kernel: kernel = Matern([1]*self.d)+WhiteKernel(noise_level_bounds=(1e-6, 1e5))
        self.GP = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10) #core SKLearn GPR
        self.repulsion0 = repulsion #initial repulsion factor
        self.repulsion = repulsion #current repulsion factor
        self.repulsion0_decay = repulsion0_decay #speed of repulsion factor decrease
        self.SamplVratio = SamplVratio #(>=1) volume from reactor end to sampling point, divided by reactor volume
        self.ObjRescaleF = 1 #objective function rescaling factor
        self.iter = -1 #current iteration number: -1 no data, 0 init, >0 actual iterations
        self.no_tau_to_SS = no_tau_to_SS
        
        #speed parameters
        if len(KXmax) == 0:
            self.KXmax = np.ones(self.d)*.3
        else:
            self.KXmax = KXmax
        self.KXmin = np.minimum(np.ones(self.d)*.05, self.KXmax)
        
        self.IntegralSample[0] = False #residence time cannot be sampled by integration (it has its own equation)
        
        # Current variation parameters
        self.X0 = []
        self.delta = []
        self.period = []
        self.phase = []
        self.texp = []
        self.Nsampl = []
        self.KX = []
        
        # History of trajectory parameters
        self.X0_hist = np.empty((0,self.d), float)
        self.delta_hist = np.empty((0,self.d), float)
        self.period_hist = np.empty((0,self.d), float)
        self.phase_hist = np.empty((0,self.d), float)
        self.texp_hist = np.empty((0,1), int)
        self.Nsampl_hist = np.empty((0,1), int)
        self.KX_hist = np.empty((0,self.d), float)
        
        # History of comparison with SS experiments
        #[dyn exp. time [min], SS exp time [min], dyn exp. reag vol / reactor vol [-], SS exp. reag vol / reactor vol [-]]
        self.SScompare_hist = np.empty((0,4), float)
        
        # History of sampled points
        self.tSampl_hist = np.empty((0,1), float)
        self.X_hist = np.empty((0,self.d), float)
        self.obj_hist = np.empty((0,1), float)
        self.best_X_hist = np.empty((0,self.d), float)
        self.best_obj_hist = np.empty((0,1), float)
        
        # History of estimated maxima
        self.best_X_estim_hist = np.empty((0,self.d), float)
        self.best_obj_estim_hist = np.empty((0,1), float)
        self.best_obj_std_estim_hist = np.empty((0,1), float)
        self.convergence_hist = []
        
        
    # ------------------------------ Domain [de-]normalization functions ------------------------------
    #   Xnorm: normalizes the value of X in [0,1]^d
    #   Xdenorm: returns the real values from a point in [0,1]^d
    # ------------------------------
    
    def Xnorm(self, X):
        return (X-self.domain[:,0])/np.diff(self.domain).T
    
    def Xdenorm(self, Xnorm):
        return self.domain[:,0]+Xnorm*np.diff(self.domain).T
    
    
    # ------------------------------ Data management ------------------------------
    #   AddExp: Updates the trajectory parameters
    #   AddResults: Adds experimental data to the history and retrains the GP
    #   AddData: Imports data from a CSV file and updates the GP
    #   Believer: (for testing) adds data to the pool based on the current trajectory and GP
    # ------------------------------
    
    def AddExp(self, X0, delta, period, phase, texp):
        self.X0 = X0
        self.delta = delta
        self.period = period
        self.phase = phase
        self.texp = texp
        self.Nsampl = int(self.texp/self.dtSampling+1)
        self.KX = 2*np.pi*self.delta*self.X0[0]/self.period
    
    def AddResults(self, t, X, Obj):
        self.iter += 1
        
        self.X0_hist = np.append(self.X0_hist, np.array([self.X0]), axis=0)
        self.delta_hist = np.append(self.delta_hist, np.array([self.delta]), axis=0)
        self.period_hist = np.append(self.period_hist, np.array([self.period]), axis=0)
        self.phase_hist = np.append(self.phase_hist, np.array([self.phase]), axis=0)
        self.texp_hist = np.append(self.texp_hist, self.texp)
        self.Nsampl_hist = np.append(self.Nsampl_hist, self.Nsampl)
        self.KX_hist = np.append(self.KX_hist, np.array([self.KX]), axis=0)
        
        self.tSampl_hist = np.append(self.tSampl_hist, t)
        self.X_hist = np.append(self.X_hist, X, axis=0)
        self.obj_hist = np.append(self.obj_hist, Obj)
        
        SScompare = self.EvalSScompare(X[:,0])
        self.SScompare_hist = np.append(self.SScompare_hist, np.array([SScompare]), axis=0)
        
        index_best = np.argmax(self.obj_hist, axis=None)
        self.best_X_hist = np.append(self.best_X_hist, np.array([self.X_hist[index_best]]), axis=0)
        self.best_obj_hist = np.append(self.best_obj_hist, self.obj_hist[index_best])
        
        self.ObjRescaleF = np.abs(self.best_obj_hist[-1])
        
        self.RefitGP()
        
        self.convergence_hist.append(self.CheckConvergence(Verbose=False))
    
    def AddData(self, csv_path, is_eff=False):
        data = pd.read_csv(csv_path, skiprows=1, header=None)
        self.Nsampl = len(data[0])
        
        len_data = len(data.columns)
        if len_data == 2: #data contains only time and objective
            print('Adding data assuming the theoretical trajectory for both instantaneous and effective variables.')
            tSampl = np.array(data[0])
            XSampl = self.Sample_X(tSampl)
            XInst = self.Xinst(np.reshape(tSampl, [-1,1]))
            ObjSampl = np.array(data[1])
        elif len_data == self.d+2:
            tSampl = np.array(data[0])
            ObjSampl = np.array(data.iloc[:,-1])
            if not is_eff:
                XSampl = self.Sample_X(tSampl)
                XInst = np.array(data.iloc[:,1:-1])
                print('The theoretical trajectory is used for effective variables.')
            else:
                XSampl = np.array(data.iloc[:,1:-1])
                XInst = self.Xinst(np.reshape(tSampl, [-1,1]))
                print('The theoretical trajectory is used for instantaneous variables.')
        else:
            raise Exception('Data size mismatch. Datafile should contain 2 or d+2 columns.')
            
        self.AddResults(tSampl, XSampl, ObjSampl)
        
        return tSampl, XSampl, XInst, ObjSampl
    
    def Believer(self):
        self.Nsampl = int(self.texp/self.dtSampling+1)
        self.Nsampl_hist = np.append(self.Nsampl_hist, self.Nsampl)
        
        tSampl = np.linspace(0,self.Nsampl-1,self.Nsampl)*self.dtSampling
        XSampl = self.Sample_X(tSampl)
        XInst = self.Xinst(np.reshape(tSampl, [-1,1]))
        ObjSampl = self.QueryGP(XSampl, False)*self.ObjRescaleF
        self.AddResults(tSampl, XSampl, ObjSampl)
        
        return tSampl, XSampl, XInst, ObjSampl
    
    
    # ------------------------------ Dynamic Experiment functions ------------------------------
    #   Xinst: returns instantaneous sinusoidal parameters
    #   Sample_X: returns the sampled trajectory conditions
    #   EvalSScompare: returns the parameters for comparison with equivalents steady conditions
    #   SuggestInit: suggests a Lissajous trajectory for intialization
    # ------------------------------

    def Xinst(self, t):
        trueVal = self.X0*(1+self.delta*np.sin(2*np.pi*np.minimum(np.maximum(t,0),self.texp)/self.period+self.phase))
        
        return trueVal
    
    def Sample_X(self, tSampl, t0=[], d=[], T=[], phi=[]):
        #by default the function samples at sample point (not at reactor outlet unless self.SamplVratio=1)
        if not t0: t0 = self.X0[0]*self.SamplVratio
        if not d: d = self.delta[0]/self.SamplVratio
        
        tauSampl = odeint(lambda tau,t: 1-self.Xinst(t-tau)[0]/self.Xinst(t)[0], self.Xinst(tSampl[0])[0]*self.SamplVratio, tSampl)
        XSampl = self.Xinst(np.reshape(tSampl, [-1,1])-tauSampl)
        
        tauRxt = odeint(lambda tau,t: 1-self.Xinst(t-tau)[0]/self.Xinst(t)[0], self.Xinst(tSampl[0])[0], tSampl)
        
        for ii,doInt in enumerate(self.IntegralSample):
            if doInt:
                for jj,t in enumerate(tSampl):
                    # Integral average Xinst from t-tauSampl[jj] to t-tauSampl[jj]+tauRxt[jj]
                    lb = t-tauSampl[jj]
                    ub = t-tauSampl[jj]+tauRxt[jj]
                    XSampl[jj,ii] = 0.
                    if lb<0:
                        if ub<=0:
                            XSampl[jj,ii] += self.Xinst(0)[ii]
                        else:
                            XSampl[jj,ii] += -self.Xinst(0)[ii]*lb/tauRxt[jj]
                            lb = 0.
                    if ub>self.texp:
                        if lb>=self.texp:
                            XSampl[jj,ii] += self.Xinst(self.texp)[ii]
                        else:
                            XSampl[jj,ii] += self.Xinst(self.texp)[ii]*(ub-self.texp)/tauRxt[jj]
                            ub = self.texp
                    if lb>=0 and ub<=self.texp:
                        XSampl[jj,ii] += self.X0[ii]/tauRxt[jj]*((ub-lb)-self.delta[ii]*self.period[ii]/2/np.pi*
                                                                 (np.cos(2*np.pi*ub/self.period[ii]+self.phase[ii])-
                                                                  np.cos(2*np.pi*lb/self.period[ii]+self.phase[ii]))
                                                                )
        
        for ii,tauR in enumerate(tauRxt):
            XSampl[ii,0] = tauR
        
        return XSampl
    
    def EvalSScompare(self, tauSampl=[]):
        if len(tauSampl)==0:
            tSampl = np.linspace(0,self.Nsampl-1,self.Nsampl)*self.dtSampling
            XSampl = self.Sample_X(tSampl)
            tauSampl = XSampl[:,0]
        
        intTauI = odeint(lambda var,t: 1/self.Xinst(t)[0]/self.SamplVratio, 0, [-self.no_tau_to_SS*self.Xinst(0)[0], self.texp])
        vol_ratio = 1/self.no_tau_to_SS/self.Nsampl*intTauI[-1,0]

        SScompare = np.array([self.texp + self.no_tau_to_SS*self.Xinst(0)[0],
                              np.sum(tauSampl)*self.no_tau_to_SS,
                              vol_ratio*self.no_tau_to_SS*self.Nsampl,
                              self.no_tau_to_SS*self.Nsampl
                             ])
        
        return SScompare
    
    def SuggestInit(self, exploration=1, period_ratio=[]):
        X0 = np.average(self.domain,1) #[mixed units]
        delta = np.diff(self.domain)[:,0]/2/X0*exploration #[-]
        
        sorted_dK = np.flip(np.sort(delta/self.KXmax))
        if not period_ratio:
            period_ratio = np.floor(np.min((1/sorted_dK[1:]*sorted_dK[0])
                                           **(1/np.array(range(1,self.d)))))
            period_ratio = np.maximum(2,period_ratio)
        
        sorted_ind = np.flip(np.argsort(delta/self.KXmax))
        exponents = (self.d-1-sorted_ind)
        NS = int(np.ceil(1+2*np.pi*X0[0]/self.dtSampling*np.max(delta/self.KXmax*period_ratio**exponents)))
        period = ((1/period_ratio)**exponents)*(NS-1)*self.dtSampling #[min]
        phase = exponents*period_ratio*np.pi/2 #[rad]
        texp = (NS-1)*self.dtSampling
        
        self.AddExp(X0, delta, period, phase, texp)
        
        tSampl = np.linspace(0,texp,NS)
        XSampl = self.Sample_X(tSampl)
        
        print('delta/Kmax')
        for ii in sorted_ind:
            print('   %s: %0.2f' % (self.var_names[ii], sorted_dK[ii]))
        print('Period ratio = %i' % (period_ratio,))
        print('Initialization will take %0.2f h.' % ((XSampl[0,0]*self.no_tau_to_SS+texp)/60,))
        
        return X0, delta, period, phase, texp, NS, tSampl, XSampl
    
    # ------------------------------ Gaussian Process functions (DynO core) ------------------------------
    #   RefitGP: trains the GP based on the current data history
    #   QueryGP: returns the average and standard deviation of the GP at given points
    #   GetGPUCB: returns the GP-UCB at given points
    #   GetAcquisitionFun: returns the acquisition function value
    #   CalculateNewTrajectory: optimizes the acquisition function based on the current data pool
    #   CheckConvergence: returns the values of the convergence criteria
    # ------------------------------
    
    def RefitGP(self):
        self.GP.fit(self.Xnorm(self.X_hist),self.obj_hist/self.ObjRescaleF)
        
        bestX, bestObj, bestObjStd = self.EstimateMax()
        self.best_X_estim_hist = np.append(self.best_X_estim_hist, np.array([bestX]), axis=0)
        self.best_obj_estim_hist = np.append(self.best_obj_estim_hist, bestObj)
        self.best_obj_std_estim_hist = np.append(self.best_obj_std_estim_hist, bestObjStd)
        
    def QueryGP(self, X, std_flag=True):
        return self.GP.predict(self.Xnorm(X), return_std=std_flag)
    
    def GetGPUCB(self, mu, std):
        delta_par = .1 #arbitrary (0,1)
        taut = 2*np.log(sum(self.Nsampl_hist)**(self.d/2+2)*np.pi**2/3/delta_par) #No-regret
        return mu + np.sqrt(taut)*std
    
    def GetAcquisitionFun(self, pars, NS_guess, dtS_guess):
        self.AddExp(pars[0:self.d],
                    pars[self.d:2*self.d],
                    pars[2*self.d:3*self.d],
                    pars[3*self.d:4*self.d],
                    (int(NS_guess*dtS_guess/self.dtSampling)-1)*self.dtSampling
                   )

        tSampl = np.linspace(0,NS_guess-1,NS_guess)*dtS_guess
        X = self.Sample_X(tSampl)

        min_distances = self.GetMinDist(self.Xnorm(X))
        dist_corr = np.exp(min(np.sum((2*self.repulsion/(np.array(min_distances)+self.repulsion))**10),1000)/NS_guess)
        
        Obj = []
        for Xtmp in X:
            mu, std = self.QueryGP(Xtmp)

            Obj.append(self.GetGPUCB(mu, std))
            NHC = 1/100
        
        return (sum(Obj) - NHC*dist_corr)/NS_guess #Returns a function to be MAXIMIZED
    
    def CalculateNewTrajectory(self, NS_guess=None, dtS_guess=None):
        self.repulsion = self.repulsion0/self.repulsion0_decay**self.iter
        print('Creating a new trajectory (based on iterations up to %i).' % (self.iter,))

        if not NS_guess: NS_guess = 3*self.d
        if not dtS_guess: dtS_guess = np.maximum((self.domain[0,0]+self.domain[0,1])/2, self.dtSampling)

        nlconstr = NonlinearConstraint(lambda pars: self.NLConstr(pars),
                                       np.append(np.append(self.domain[:,0], self.domain[:,0]), self.KXmin),
                                       np.append(np.append(self.domain[:,1], self.domain[:,1]), self.KXmax)
                                      )
        #delta cannot be negative
        bnd = Bounds(lb=np.append(np.append(np.append(self.domain[:,0], [0]*self.d), [dtS_guess*2]*self.d), [-np.pi]*self.d),
                     ub=np.append(np.append(np.append(self.domain[:,1], [10]*self.d), [(NS_guess-1)*dtS_guess*4]*self.d), [np.pi]*self.d)
                    )

        res = differential_evolution(lambda pars: -self.GetAcquisitionFun(pars, NS_guess, dtS_guess),
                                     bnd,
                                     constraints=nlconstr,
                                     tol=0.05,
                                     popsize=20,
                                     polish=False
                                    )
        
        X0 = res.x[0:self.d]
        delta = res.x[self.d:2*self.d]
        period = res.x[2*self.d:3*self.d]
        phase = res.x[3*self.d:4*self.d]
        NS = int(NS_guess*dtS_guess/self.dtSampling)
        texp = (NS-1)*self.dtSampling
        
        self.AddExp(X0, delta, period, phase, texp)
        
        tSampl = np.linspace(0,texp,NS)
        XSampl = self.Sample_X(tSampl)
        
        return X0, delta, period, phase, texp, NS, tSampl, XSampl
    
    def CheckConvergence(self, Verbose=True):
        if self.iter>0:
            criteria_names = ['Measured and estimated objectives have similar value (10% significance level)',
                              'Measured and estimated objectives are close in the design space (< %0.3f)' % (self.repulsion0),
                              'Estimated objective value has low uncertainty (sigma-sigma_n < 5%)',
                              'Estimated objective location has not moved significantly (< %0.3f)' % (self.repulsion0)
                             ]
            criteria = [2*norm.cdf(-abs(self.best_obj_hist[-1]-self.best_obj_estim_hist[-1])/self.best_obj_std_estim_hist[-1])>.1,
                        L2norm(self.Xnorm(self.best_X_estim_hist[-1])-self.Xnorm(self.best_X_hist[-1]))<self.repulsion0,
                        abs((self.best_obj_std_estim_hist[-1]-self.GP.kernel_.get_params()['k2__noise_level']**.5*self.ObjRescaleF)/self.best_obj_estim_hist[-1])<.05,
                        L2norm(self.Xnorm(self.best_X_estim_hist[-2])-self.Xnorm(self.best_X_estim_hist[-1]))<self.repulsion0
                       ]
            text_result = ['Best value: %0.2f measured | %0.2f estimated' % (self.best_obj_hist[-1],
                                                                             self.best_obj_estim_hist[-1]
                                                                            ),
                           'Best location: ' + str(np.round(self.best_X_hist[-1],2)) + ' measured | ' + str(np.round(self.best_X_estim_hist[-1],2)) + ' estimated',
                           'Estimated optimum: %0.2f \u00B1 %0.2f (mu \u00B1 sigma)' % (self.best_obj_estim_hist[-1],
                                                                              self.best_obj_std_estim_hist[-1]
                                                                              ),
                           'Estimated optimum location: ' + str(np.round(self.best_X_estim_hist[-1],2)) + ' at iter. %i | ' % (self.iter,) + str(np.round(self.best_X_estim_hist[-2],2)) + ' at iter. %i' % (self.iter-1,)
                          ]
            
            if Verbose:
                print('Convergence checks:')
                for ii,c in enumerate(criteria):
                    print('\t', criteria_names[ii], end='... ')
                    if c:
                        print('Passed.')
                    else:
                        print('Failed.')
                        print('\t\t', text_result[ii])
                
                if all(criteria):
                    print('\n1i4c criterion satisfied at iteration %i. Regret estimate < 1%%' % (self.iter,))
                elif sum(criteria)==3:
                    print('\n1i3c criterion satisfied at iteration %i. Regret estimate < 2%%' % (self.iter,))
                elif sum(criteria)==2 and self.iter>=2:
                    print('\n2i2c criterion satisfied at iteration %i. Regret estimate < 2.5%%' % (self.iter,))
                elif sum(criteria)==1 and self.iter>=2:
                    print('\n2i1c criterion satisfied at iteration %i. Regret estimate < 3%%' % (self.iter,))
        else:
            criteria = [False]*4
            if Verbose:
                print('At least one iteration after initialization should be done to check convergence.')
        
        return criteria
    
    
    
    # ------------------------------ Auxiliary functions ------------------------------
    #   GetMinDist: calculates the minimum normalized distances
    #   NLConstr: nonlinear constraints on new trajectories
    #   EstimateMax: evaluates the maximum of the GP in the domain
    #   GetEI: returns the expected improvement at given points
    # ------------------------------
    
    def GetMinDist(self, Xnorm):
        NS = len(Xnorm)
        min_distances = []
        for ii in range(NS):
            distances = []
            for jj in range(NS): #cycle over points of the trajectory
                if not jj == ii:
                    distances.append(L2norm(Xnorm[ii,:]-Xnorm[jj,:]))
            for jj in range(len(self.obj_hist)): #cycle over already-known points
                distances.append(L2norm(Xnorm[ii,:]-self.X_hist[jj]))
            min_distances.append(min(distances))

        return min_distances
    
    def NLConstr(self, pars):
        X0 = pars[0:self.d]
        delta = pars[self.d:2*self.d]
        period = pars[2*self.d:3*self.d]
        phase = pars[3*self.d:4*self.d]
        
        return np.append(np.append(X0*(1+delta),
                                   X0*(1-delta)
                                  ),
                         2*np.pi*delta/period*X0[0]
                        )
    
    def EstimateMax(self):
        bnd = Bounds(lb=self.domain[:,0],ub=self.domain[:,1])
        res = differential_evolution(lambda X: -self.QueryGP(X, False),
                                     bounds=bnd
                                    )
        ObjOpt, ObjStd = self.QueryGP(res.x)
        
        return res.x, ObjOpt*self.ObjRescaleF, ObjStd*self.ObjRescaleF
    
    def GetEI(self, mu, std):
        ZZ = (mu-max(self.obj_hist))/std
        return ((mu-max(self.obj_hist))*norm.cdf(ZZ) + std*norm.pdf(ZZ))*(std>0)
    
    
    # ------------------------------ Display functions ------------------------------
    #   PlotTrajectory: plots the values of the optimization parameters over time based on the current trajectory and displays the objective
    #   PlotEstimate: returns the GP-evaluated objective funcion (if domain is 2D) or its projection (if domain has dimensionality > 2)
    # ------------------------------
    
    def PlotTrajectory(self, tSampl=[], XSampl=[], XInst=[], ObjSampl=[], PlotEI=False, PlotUCB=False, Verbose=True):
        tRxt = np.linspace(-self.no_tau_to_SS*self.Xinst(0)[0],self.texp,300)
        XRxt = self.Sample_X(tRxt)
        ObjRxt, StdRxt = self.QueryGP(XRxt)
        ObjRxt *= self.ObjRescaleF
        StdRxt *= self.ObjRescaleF
        
        if (len(tSampl) == 0 or len(XSampl) == 0 or len(ObjSampl)==0) and not len(self.X_hist)==0:
            data_range = range(np.sum(self.Nsampl_hist[:-1]),np.sum(self.Nsampl_hist))
            tSampl = self.tSampl_hist[data_range]
            XSampl = self.X_hist[data_range,:]
            ObjSampl = self.obj_hist[data_range]
            XInst = self.Xinst(np.reshape(tSampl, [-1,1]))
        
        fig = plt.figure(figsize=((self.d+1)*5.5,3))
        for ii in range(self.d):
            plt.subplot(1,self.d+1,ii+1)
            plt.plot(tRxt/60, self.Xinst(np.reshape(tRxt, [-1,1]))[:,ii], 'b-')
            plt.plot(tSampl/60, XInst[:,ii], 'bo')
            plt.plot(tRxt/60, XRxt[:,ii], 'k:')
            plt.plot(tSampl/60, XSampl[:,ii], 'k*')
            plt.ylim(self.domain[ii])
            plt.xlabel('Time [h]')
            plt.ylabel(self.var_names[ii])
            plt.title('K_X = %0.2f' % self.KX[ii])
        
        plt.subplot(1,self.d+1,self.d+1)
        plt.plot(tSampl/60, ObjSampl, 'k*')
        plt.plot(tRxt/60, ObjRxt, 'k:')
        plt.fill_between(tRxt/60, ObjRxt+StdRxt, ObjRxt-StdRxt, color='b', alpha=.2)
        plt.xlabel('Time [h]')
        plt.ylabel('Objective')
        plt.show()

        if not len(self.X_hist)==0:
            self.PlotEstimate(XRxt=XRxt, XSampl=XSampl, ObjSampl=ObjSampl, PlotEI=PlotEI, PlotUCB=PlotUCB)
            plt.show()
        
            if Verbose:
                print('Current optima: %0.2f measured at' % (self.best_obj_hist[-1]), np.round(self.best_X_hist[-1],2) ,'| %0.2f\u00B1%0.2f estimated at' % (self.best_obj_estim_hist[-1], 2*self.best_obj_std_estim_hist[-1]), np.round(self.best_X_estim_hist[-1],2))
                min_distances = self.GetMinDist(self.Xnorm(XSampl))
                print('Distance/repulsion range: %0.2f - %0.2f' % (min(min_distances)/self.repulsion,max(min_distances)/self.repulsion))
                
    def PlotEstimate(self, XRxt=[], XSampl=[], ObjSampl=[], PlotEI=False, PlotUCB=False):
        if self.d==2:
            x1 = np.linspace(self.domain[0,0],self.domain[0,1],70)
            x2 = np.linspace(self.domain[1,0],self.domain[1,1],50)
            mu_estim = np.zeros([50,70])
            std_estim = np.zeros([50,70])
            for ii in range(70):
                for jj in range(50):
                    mu_estim[jj,ii], std_estim[jj,ii] = self.QueryGP(np.array([x1[ii], x2[jj]]))
            mu_estim = mu_estim*self.ObjRescaleF
            std_estim = std_estim*self.ObjRescaleF

            PlotObj=False
            if not len(ObjSampl)==0: PlotObj=True

            nplots = 2+PlotEI+PlotUCB
            fig = plt.figure(figsize=(5.5*nplots,3+PlotObj*5))
            fig.add_subplot(1+PlotObj,nplots,1)
            plt.contourf(x1,x2,mu_estim)
            plt.colorbar()
            plt.plot(self.X_hist[:,0],self.X_hist[:,1], 'k.')
            if not len(XRxt)==0: plt.plot(XRxt[:,0],XRxt[:,1], 'r:')
            if not len(XSampl)==0: plt.plot(XSampl[:,0],XSampl[:,1], 'r*')
            plt.xlabel(self.var_names[0])
            plt.ylabel(self.var_names[1])
            plt.title('Estimated objective')

            fig.add_subplot(1+PlotObj,nplots,2)
            plt.contourf(x1,x2,std_estim)
            plt.colorbar()
            plt.plot(self.X_hist[:,0],self.X_hist[:,1], 'k.')
            if not len(XRxt)==0: plt.plot(XRxt[:,0],XRxt[:,1], 'r:')
            if not len(XSampl)==0: plt.plot(XSampl[:,0],XSampl[:,1], 'r*')
            plt.xlabel(self.var_names[0])
            plt.ylabel(self.var_names[1])
            plt.title('Estimated standard dev.')

            plothere = 2
            if PlotEI:
                plothere +=1
                EI = self.GetEI(mu_estim, std_estim)

                fig.add_subplot(1+PlotObj,nplots,plothere)
                plt.contourf(x1,x2,EI)
                plt.colorbar()
                plt.plot(self.X_hist[:,0],self.X_hist[:,1], 'k.')
                if not len(XRxt)==0: plt.plot(XRxt[:,0],XRxt[:,1], 'r:')
                if not len(XSampl)==0: plt.plot(XSampl[:,0],XSampl[:,1], 'r*')
                plt.xlabel(self.var_names[0])
                plt.ylabel(self.var_names[1])
                plt.title('EI')
            if PlotUCB:
                plothere +=1
                GPUCB = self.GetGPUCB(mu_estim, std_estim)

                fig.add_subplot(1+PlotObj,nplots,plothere)
                plt.contourf(x1,x2,GPUCB)
                plt.colorbar()
                plt.plot(self.X_hist[:,0],self.X_hist[:,1], 'k.')
                if not len(XRxt)==0: plt.plot(XRxt[:,0],XRxt[:,1], 'r:')
                if not len(XSampl)==0: plt.plot(XSampl[:,0],XSampl[:,1], 'r*')
                plt.xlabel(self.var_names[0])
                plt.ylabel(self.var_names[1])
                plt.title('GP-UCB')
            if PlotObj:
                plothere +=1

                X1,X2 = np.meshgrid(x1,x2)

                angles = 3
                for ii in range(angles):
                    ax = fig.add_subplot(1+PlotObj,angles,angles+ii+1, projection='3d')
                    ax.view_init(30, 360/angles*(ii*1))
                    ax.plot_surface(X1,X2,mu_estim, alpha=.5, cmap='viridis')
                    ax.plot(self.X_hist[:,0],self.X_hist[:,1],self.obj_hist, 'k.')
                    if not len(XSampl)==0: ax.plot(XSampl[:,0],XSampl[:,1],ObjSampl, 'r*:')
                    ax.set_xlabel(self.var_names[0])
                    ax.set_ylabel(self.var_names[1])
                    ax.set_zlabel('Objective')
                    
        elif self.d>2:
            tmpsampler = np.random.rand(1000,self.d)
            Xplot = self.Xdenorm(tmpsampler)
            (estimObjNorm, estimStdNorm) = self.QueryGP(Xplot)

            estimObj = estimObjNorm*self.ObjRescaleF
            estimStd = estimStdNorm*self.ObjRescaleF

            if PlotUCB: fig = plt.figure(figsize=(5*self.d,10))
            else: fig = plt.figure(figsize=(5*self.d,5))
            for ii in range(self.d):
                if PlotUCB: ax = fig.add_subplot(2,self.d,ii+1)
                else: ax = fig.add_subplot(1,self.d,ii+1)
                scattplot = ax.scatter(Xplot[:,ii], estimObj, s=4, c=estimStd, alpha=.4, marker='o', cmap='jet', vmin=0)
                ax.plot(self.X_hist[:,ii], self.obj_hist, 'k.')
                if not len(XSampl)==0: ax.plot(XSampl[:,ii], ObjSampl, '*r')
                ax.set_xlabel(self.var_names[ii])
                ax.set_ylabel('Objective')

                if PlotUCB:
                    ax = fig.add_subplot(2,self.d,self.d+ii+1)
                    ax.scatter(Xplot[:,ii],self.GetGPUCB(estimObj,estimStd), s=4, c=estimStd, alpha=.4, marker='o', cmap='jet', vmin=0)
                    ax.set_xlabel(self.var_names[ii])
                    ax.set_ylabel('GP-UCB')

            fig.subplots_adjust(right=0.9)
            cbar_ax = fig.add_axes([0.93, 0.15, 0.01, 0.7])
            fig.colorbar(scattplot, cax=cbar_ax, label='GP standard deviation')