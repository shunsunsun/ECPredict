[![UML Energy & Combustion Research Laboratory](http://faculty.uml.edu/Hunter_Mack/uploads/9/7/1/3/97138798/1481826668_2.png)](http://faculty.uml.edu/Hunter_Mack/)

# ECPredict: Pre-built predictive models for a variety of fuel properties

[![GitHub version](https://badge.fury.io/gh/ecrl%2FECPredict.svg)](https://badge.fury.io/gh/ecrl%2FECPredict)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/ECRL/ECPredict/master/LICENSE.txt)
[![Build Status](https://dev.azure.com/uml-ecrl/package-management/_apis/build/status/ECRL.ECPredict?branchName=master)](https://dev.azure.com/uml-ecrl/package-management/_build/latest?definitionId=4&branchName=master)

**ECPredict** is an open source Python package containing pre-built models for predicting fuel properties developed by the UMass Lowell Energy and Combustion Research Laboratory team using [ECNet](https://github.com/ecrl/ecnet). ECPredict currently offers predictive models for the following fuel properties:
- [Cetane number](https://en.wikipedia.org/wiki/Cetane_number)
- [Cloud point](https://en.wikipedia.org/wiki/Cloud_point)
- [Kinematic viscosity](https://en.wikipedia.org/wiki/Viscosity#Dynamic_and_kinematic_viscosity)
- [Motor octane number](https://en.wikipedia.org/wiki/Octane_rating#Motor_Octane_Number_(MON))
- [Octane sensitivity](https://en.wikipedia.org/wiki/Octane_rating#Difference_between_RON,_MON,_and_AKI)
- [Pour point](https://en.wikipedia.org/wiki/Pour_point)
- [Research octane number](https://en.wikipedia.org/wiki/Octane_rating#Research_Octane_Number_(RON))
- [Yield sooting index](https://www.sciencedirect.com/science/article/pii/S0010218017304728)

To cite this tool, cite [ECNet](https://joss.theoj.org/papers/10.21105/joss.00401).

# Installation

ECPredict must be installed from source. To install from source, download the repository and run _setup.py_ in your command line/terminal/Python environment:

```
git clone https://github.com/ecrl/ecpredict
cd ecpredict
python setup.py install
```

ECPredict requires three dependencies: [TensorFlow](https://github.com/tensorflow/tensorflow), [alvaDescPy](https://github.com/ECRL/alvaDescPy), and [PaDELPy](https://github.com/ECRL/PaDELPy). If TensorFlow is already installed in your Python environment, you can run _setup.py_ without installing TensorFlow:

```
python setup.py --omit_tf install
```

# Usage

First, import the function for the fuel property you want to predict:

```python
# Predict cetane number
from ecpredict import cetane_number

# Predict cloud point
from ecpredict import cloud_point

# Predict kinematic viscosity
from ecpredict import kinematic_viscosity

# Predict motor octane number
from ecpredict import motor_octane_number

# Predict octane sensitivity
from ecpredict import octane_sensitivity

# Predict pour point
from ecpredict import pour_point

# Predict research octane number
from ecpredict import research_octane_number

# Predict yield sooting index
from ecpredict import yield_sooting_index
```

Each function accepts two arguments: a list of SMILES strings, and the backend software used to perform input variable generation. Each function returns a tuple containing the predictions for the supplied SMILES strings (list), and the expected error of the prediction (median absolute error of test set predictions, float):

```python
smiles = ['CCC', 'CCCCC']

# Use PaDEL-Descriptor for input variable generation
predictions, error = cetane_number(smiles)
print(predictions, error)

# Use alvaDesc for input variable generation
predictions, error = cetane_number(smiles, 'alvadesc')
print(predictions, error)
```

```
[26.317856, 24.589973] 6.064
[23.902477, 30.3196] 5.1397
```

Current backend software includes [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/) and [alvaDesc](https://www.alvascience.com/alvadesc/). The default backend software used is PaDEL-Descriptor, and is installed alongside ECPredict. Note that an installation of Java JRE is required to run the PaDEL-Descriptor software. Using alvaDesc requires a valid license.

More information regarding the predictive performance of each model is outlined in the [docs](docs/README.md) directory.

# Contributing, Reporting Issues and Other Support:

To contribute to ECPredict, make a pull request. Contributions should include tests for new features added, as well as extensive documentation.

To report problems with the software or feature requests, file an issue. When reporting problems, include information such as error messages, your OS/environment and Python version.

For additional support/questions, contact Travis Kessler (Travis_Kessler@student.uml.edu) and/or John Hunter Mack (Hunter_Mack@uml.edu).
