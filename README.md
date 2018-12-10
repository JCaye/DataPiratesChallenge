[![CircleCI](https://circleci.com/gh/JCaye/DataPiratesChallenge/tree/master.svg?style=svg)](https://circleci.com/gh/JCaye/DataPiratesChallenge/tree/master) [![codecov](https://codecov.io/gh/JCaye/DataPiratesChallenge/branch/master/graph/badge.svg)](https://codecov.io/gh/JCaye/DataPiratesChallenge)
# DataPiratesChallenge
Solution to the Data Pirates Challenge

# What is this?
This application retrieves postal code ranges ("faixa de CEP") for up to 100 locations on any 2 states of Brazil. The data is read from the [brazilian postal services website](http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm).

# Why is <del>gamora</del> this?
Well, why not?

# How to use it?
Clone the repo and set up your python vituralenv with `virtualenv venv -p python` (make sure to run python 3.7). Once there, activate the venv with `./venv/scripts/activate.bat` and install the requirements with `pip install -r requirements.txt`.
Finally, with everything setup, run `python ./src/cep/buscarCep.py STATE1 STATE2`. The script will collect information on the two specified states (use only their acronyms), and save it to `out/` folder as `.jsonl` files.

# Output files
The files are written as `jsonlines`, each line corresponding to one range of postal codes. Each element has two attributes: location (`localidade`) and the range of postal code (`faixa de CEP`).
