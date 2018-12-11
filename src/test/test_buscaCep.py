import pytest

from src.cep.buscaCep import buildFormData, getDataFromUrl, readDataFromHtmlTable, writeToFile, getPostalCodeInfo

def test_buildFormData_whenValidArgs_thenSuccess():
	assert buildFormData('SC', 50) == {
									'UF': 'SC',
									'qtdrow': 51
									}
def test_buildFormData_whenNoLenght_thenUseDefault():
	assert buildFormData('DF') == {
									'UF': 'DF',
									'qtdrow': 101
									}

def test_buildFormData_whenNonPositivoRows_thenAssertionError():
	with pytest.raises(AssertionError) as e_info:
		buildFormData('SC', -2)

def test_buildFormData_whenInvalidState_thenAssertionError():
	with pytest.raises(AssertionError) as e_info:
		buildFormData('invalidState')

def test_buildFormData_whenInvalidRows_thenFail():
	with pytest.raises(AssertionError) as e_info:
		buildFormData('SC', -12)

def test_getDataFromUrl_whenValidFormData_thenSuccess():
	try:
		getDataFromUrl(formData = buildFormData('SP', 100))
	except:
		assert False

def test_readDataFromHtmlTable_whenValidTable_thenSuccess():
	assert 40 == len(
				readDataFromHtmlTable(
					getDataFromUrl(
						formData=buildFormData('SP')
					),
					qtdrow=40
				)
			)