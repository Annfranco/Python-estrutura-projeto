import os

from models.pessoa import Pessoa
from models.endereco import Endereco
from models.enums.sexo import Sexo
from models.enums.unidade_federativa import UnidadeFederativa

os.system("cls||clear")

pessoa_1 = Pessoa(4011, "Marta", "08/12/1995", "7198541-7984", "baestar@gmail.com", Sexo.FEMININO, 
                  Endereco("Rua A", 101, "2 andar", "41987-200", "Salvador", UnidadeFederativa.BAHIA))

print(pessoa_1)
