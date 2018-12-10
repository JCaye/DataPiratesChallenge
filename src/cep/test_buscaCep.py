import pytest

from buscaCep import buildFormData, getDataFromUrl, readDataFromHtmlTable, writeToFile

def test_buildFormData_whenValidArgs_thenSuccess():
	assert buildFormData('SC', 50) == {
									'UF': 'SC',
									'qtdrow': 50
									}