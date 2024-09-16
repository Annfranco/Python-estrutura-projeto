import pytest
from atividade1.models.pessoa import Pessoa # caminho absoluto
# from ..models.endereco import Endereco # caminho relativo
from atividade1.models.endereco import Endereco 
from atividade1.models.enums.sexo import Sexo
from atividade1.models.enums.unidade_federativa import UnidadeFederativa

# Modelo
@pytest.fixture
def criar_pessoa():
    pessoa_1 =  Pessoa(4011, "Marta", "08/12/1995", "7198541-7984", "baestar@gmail.com", Sexo.FEMININO, 
                  Endereco("Rua A", 101, "2 andar", "41987-200", "Salvador", UnidadeFederativa.BAHIA))
    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Marta"

def test_pessoa_atributo_id(criar_pessoa):
    assert criar_pessoa.id == 4011

def test_endereco_logradouro_de_pessoa(criar_pessoa):
    assert criar_pessoa.endereco.logradouro == "Rua A"
