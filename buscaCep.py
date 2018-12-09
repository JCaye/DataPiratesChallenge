import os
import requests
import pandas as pd

from bs4 import BeautifulSoup

allowedStates = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
			'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
			'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

def buildFormData(uf, qtdrow = 100):
	return {
			'UF': uf,
			'qtdrow': qtdrow
			}

def getDataFromUrl(url='http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm', formData={}):
	r = requests.post(url, data=formData)
	if r.status_code != 200:
		raise RuntimeError('Request was not successful')
	return BeautifulSoup(r.content, 'html.parser').findAll('table')[1]

def readDataFromHtmlTable(htmlTable):
	return [
			{
			'Localidade': table_row.findAll('td')[0].get_text(),
			'Faixa de CEP': table_row.findAll('td')[1].get_text()
			} 
			for table_row in htmlTable.findAll('tr')[2:]
			]

def writeToFile(listOfDicts, fileName):
	pd.DataFrame(listOfDicts).to_json(path_or_buf=fileName + '.jsonl', orient='records', lines=True)

def main():
	states = [os.environ.get('STATE1', 'SP'), os.environ.get('STATE2', 'RJ')]
	for state in states:
		if state not in allowedStates:
			raise ValueError("Invalid state acronym providaded")
		writeToFile(
			listOfDicts=readDataFromHtmlTable(
				getDataFromUrl(
					url='http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm',
					formData=buildFormData(uf=state)
				)
			),
			fileName=state
		)

if __name__ == '__main__':
	main()
