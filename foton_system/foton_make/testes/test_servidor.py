import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from pandas import DataFrame, ExcelFile
from .cliente_library import BaseServidor, Verificador, Gerenciador, ConfigError, DatabaseError, FilesystemError

# Caminho fictício para os testes
caminho_base_teste = Path("/fakepath/base_clientes.xlsx")
caminho_pasta_teste = Path("/fakepath/pastas_clientes")

@pytest.fixture
def servidor():
    config_teste = {'caminho_pastaClientes': caminho_pasta_teste, 'caminho_baseClientes': caminho_base_teste}
    servidor = BaseServidor()
    servidor.pastaClientes = caminho_pasta_teste
    servidor.baseClientes = caminho_base_teste
    return servidor

def test_inicializacao_correta(servidor):
    assert servidor.pastaClientes == caminho_pasta_teste
    assert servidor.baseClientes == caminho_base_teste

def test_erro_de_configuracao_faltante():
    with pytest.raises(ConfigError):
        BaseServidor()

@patch('pathlib.Path.exists')
def test_verificar_existencia_base(mock_exists, servidor):
    mock_exists.return_value = True
    verificador = Verificador()
    assert verificador.base_existe() is None

@patch('pathlib.Path.is_dir')
def test_verificar_diretorio_cliente(mock_is_dir, servidor):
    mock_is_dir.return_value = True
    verificador = Verificador()
    assert verificador.pasta_clientes_existe() is None

@patch('pandas.read_excel', return_value=DataFrame({'Alias': ['Cliente1', 'Cliente2']}))
def test_obter_aliases(mock_read_excel, servidor):
    verificador = Verificador()
    aliases = verificador.obter_aliases()
    assert aliases == ['Cliente1', 'Cliente2']

@patch('pandas.read_excel')
@patch('pathlib.Path.iterdir')
def test_verificar_pastas_clientes(mock_iterdir, mock_read_excel, servidor):
    mock_read_excel.return_value = DataFrame({'Alias': ['Cliente1', 'Cliente2', 'Cliente3']})
    mock_iterdir.return_value = [Path("/fakepath/pastas_clientes/Cliente1"), Path("/fakepath/pastas_clientes/Cliente2")]
    gerenciador = Gerenciador()
    faltantes = gerenciador.verificar_pastas_clientes()
    assert faltantes == {'Cliente3'}
