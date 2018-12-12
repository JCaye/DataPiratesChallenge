[![CircleCI](https://circleci.com/gh/JCaye/DataPiratesChallenge/tree/master.svg?style=svg)](https://circleci.com/gh/JCaye/DataPiratesChallenge/tree/master) [![codecov](https://codecov.io/gh/JCaye/DataPiratesChallenge/branch/master/graph/badge.svg)](https://codecov.io/gh/JCaye/DataPiratesChallenge)
# DataPiratesChallenge
Solution to the Data Pirates Challenge

# What is this?
This application retrieves postal code ranges ("faixa de CEP") for up to 100 locations on any 2 states of Brazil. The data is read from the [brazilian postal services website](http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm).

# Why is <del>gamora</del> this?
Well, why not?

# How to use it?
Clone the repo and run `make build run STATES="STATE1 STATE2 STATE3 ..."` from the `DataPiratesChallenge` directory. STATES are optional variables which map to specific brazilian states (uppercase 2-letter inputs are valid). If no STATE is provided, the default values will be `SP` and `RJ`. If an invalid state is provided, the application will exit without running.

Alternatively, in the abscence of either docker or make, you can spin up your own virtualenv with `virtualenv venv -p python`(make sure to use python 3.7), install the required dependencies with `pip install -r requirements.txt` and run the app with `python ./src/cep/buscaCep.py STATE1 STATE2 ...` (this will require you to pass at least one argument).

# Output files
The files are written as `jsonlines` to `out` folder, each line corresponding to one range of postal codes. Each element has two attributes: location (`localidade`) and the range of postal code (`faixa de CEP`).
