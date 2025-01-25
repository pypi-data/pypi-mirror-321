![logo](DynOpt_logo.svg)

# DynOpt
DynOpt is a toolbox for chemical reaction optimization using dynamic experiments in a flow-chemistry setup, leveraging Bayesian optimization to suggest new dynamic experiments to perform in an experimental setup.

Data provided to the algorithm can come from both steady or dynamic experiments under different conditions (<i>e.g.</i>, composition, temperature, residence time, ...) in a continuous/Euclidean chemical design space. The algorithm will provide a trajectory (optimization parameters as a function of time) to explore such design space. Such trajectory can be run experimentally using a single dynamic experiment or (less efficiently) with a series of steady experiments in discrete location of the trajectory. After providing the new data to the algorithm (re-training), the procedure is repeated until the algorithm stopping criteria are met.

DynO (a tool for single objective optimization) is compatible with Python 3 (>= 3.6). For details about theory see the paper on [dynamic experiments](http://dx.doi.org/10.1039/D1RE00350J) and the one on [optimization](http://dx.doi.org/10.1039/D4RE00543K).

## Installation
Pip installable package:

`pip install DynOpt`

PyPI: [DynOpt](https://pypi.org/project/DynOpt/)

### Dependencies
- Math
  - numpy (1.19.5)
  - scipy (1.7.3)
- Gaussian Processes
  - scikit-learn (0.24.2)
- Data management
  - pandas (1.1.5)
- Display
  - matplotlib (3.3.4)

## Use
Refer to the [Wiki](https://github.com/fflorit/DynOpt/wiki) and the [examples](https://github.com/fflorit/DynOpt/tree/main/examples).

&nbsp;

## Contributors
Federico Florit: [github](https://github.com/fflorit)

## Citation
If you use any part of this code in your work, please cite the [paper](http://dx.doi.org/10.1039/D4RE00543K).
```
@article{DynO,
  author  = {Florit, Federico and Nandiwale, Kakasaheb Y. and Armstrong, Cameron T. and Grohowalski, Katharina and Diaz, Angel R. and Mustakis, Jason and Guinness, Steven M. and Jensen, Klavs F.},
  title   = {Dynamic flow experiments for Bayesian optimization of a single process objective},
  journal = {React. Chem. Eng.},
  year    = {2025},
  volume  = {-},
  number  = {-},
  pages   = {-},
  doi  = {10.1039/D4RE00543K}
}
```

## License
This software is released under a BSD 3-Clause license. For more details, please refer to
[LICENSE](https://github.com/fflorit/DynOpt/blob/main/LICENSE).

"Copyright 2025 Federico Florit"
