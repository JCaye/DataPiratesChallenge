import os
import sys
import json
import requests

from bs4 import BeautifulSoup


def getAllowedStates(url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm'):
	r = requests.get(url)
	if r.status_code != 200:
		raise RuntimeError('Request was not successful')
	
	stateHtmlContainers = BeautifulSoup(r.content, 'html.parser').find('select').option.children
	return set([state.get_text() for state in stateHtmlContainers if state != " "])


def buildFormData(uf, qtdrow = 100):
	assert qtdrow >= 0
	return {
			'UF': uf,
			'qtdrow': qtdrow + 1
			}


def getDataFromUrl(url='http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm', formData={}):
	r = requests.post(url, data=formData)
	if r.status_code != 200:
		raise RuntimeError('Request was not successful')
	return BeautifulSoup(r.content, 'html.parser').findAll('table')[1]


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


def getPostalCodeInfo(states):
	if not os.path.exists('out'):
		os.makedirs('out')
	
	for state in states:
		print('Collecting data for', state)
		writeToFile(
			listOfDicts=readDataFromHtmlTable(
				getDataFromUrl(
					url='http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm',
					formData=buildFormData(uf=state)
				)
			),
			fileName=state
		)

		
def main(states):
	getPostalCodeInfo(states)

if __name__ == '__main__':
	if not (len(sys.argv[1:]) > 0):
		print('Usage: buscaCep.py STATE1 STATE2 STATE3 ...')
		quit(code=1)
	allowedStates = getAllowedStates()
	if len(set(sys.argv[1:]) - allowedStates) != 0:
		print("These are not valid states", set(sys.argv[1:]) - allowedStates)
		quit(code=2)
	main(sys.argv[1:], allowedStates)