import os

from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco 

os.system("cls||clear")

# Instanciando Classe.
pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO, Endereco("Rua A", 10))

print(pessoa_1)