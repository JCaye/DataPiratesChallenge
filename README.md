# DataPiratesChallenge
Solution to the Data Pirates Challenge

# What is this?
This application retrieves postal code ranges ("faixa de CEP") for up to 100 locations on any 2 states of Brazil. The data is read from the [brazilian postal services website](http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm).

# Why is <del>gamora</del> this?
Well, why not?

# How to use it?
Clone the repo and set up your python vituralenv with `virtualenv venv -p python` (make sure to run python 3.7). Once there, activate the venv with `./venv/scripts/activate.bat` and install the requirements with `pip install -r requirements.txt`.
Finally, with everything setup, run `python ./src/cep/buscarCep.py`. The script will collect information on two default states, and save it to `out/` folder, as `.jsonl` files.

# Querying non-default states
To collect data for other states than the default ones, set environment variables called `STATE1` and/or `STATE2` to the two letter acronym for the state of interest, and run the application again.

# Output files
The files are written as `jsonlines`, each line corresponding to one range of postal codes. Each element has two attributes: location (`localidade`) and the range of postal code (`faixa de CEP`).
