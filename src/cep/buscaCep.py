import os
import sys
import json
import requests

from bs4 import BeautifulSoup

allowedStates = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
			'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
			'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

def buildFormData(uf, qtdrow = 100):
	assert uf in allowedStates
	assert qtdrow >= 0
	return {
			'UF': uf,
			'qtdrow': qtdrow + 1
			}

def getDataFromUrl(url='http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm', formData={}):
	r = requests.post(url, data=formData)
	if r.status_code != 200:
		raise RuntimeError('Request was not successful')
	return BeautifulSoup(r.content.decode('ISO-8859-1'), 'html.parser').findAll('table')[1]

def readDataFromHtmlTable(htmlTable, qtdrow = 100):
	return [
			{
			'Localidade': table_row.findAll('td')[0].get_text(),
			'Faixa de CEP': table_row.findAll('td')[1].get_text()
			} 
			for table_row in htmlTable.findAll('tr')[2:2+qtdrow]
			]

def writeToFile(listOfDicts, fileName):
	with open('./out/{}.jsonl'.format(fileName), 'w+') as output:
		for line in listOfDicts:
			output.write(json.dumps(line) + '\n')

def main(state1='SP', state2='RJ'):
	if not os.path.exists('out'):
		os.makedirs('out')
	
	for state in [state1, state2]:
		print('Collecting data for', state)
		if state not in allowedStates:
			print('No state named', state)
			raise ValueError('No state named %s' % state)
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
	if len(sys.argv) != 3:
		print('Usage: python ./src/cep/buscaCep.py STATE1 STATE2')
	else:
		main(sys.argv[1], sys.argv[2])
