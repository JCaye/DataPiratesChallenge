[![CircleCI](https://circleci.com/gh/JCaye/DataPiratesChallenge/tree/master.svg?style=svg)](https://circleci.com/gh/JCaye/DataPiratesChallenge/tree/master) [![codecov](https://codecov.io/gh/JCaye/DataPiratesChallenge/branch/master/graph/badge.svg)](https://codecov.io/gh/JCaye/DataPiratesChallenge)
# DataPiratesChallenge
Solution to the Data Pirates Challenge

# What is this?
This application retrieves postal code ranges ("faixa de CEP") for up to 100 locations on any 2 states of Brazil. The data is read from the [brazilian postal services website](http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm).

# Why is <del>gamora</del> this?
Well, why not?

# How to use it?
Clone the repo and run `make build run STATE1 STATE2 STATE3 ...`. STATES are optional variables which map to specific brazilian states. If no STATE is provided, or if an invalid state is provided, the application will exit without running.

# Output files
The files are written as `jsonlines` to `out` folder, each line corresponding to one range of postal codes. Each element has two attributes: location (`localidade`) and the range of postal code (`faixa de CEP`).
