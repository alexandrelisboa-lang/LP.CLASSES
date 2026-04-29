import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome:str
    email:str
    telefone:int

@dataclass
class Funcionario:
    nome:str
    matricula:str
    email:str
    setor:str


cliente1 = Cliente('maria','maria@gmail.com','7197687909')

funcionario1=Funcionario('xandy','23052008','xandy003@gmail.com','gerente')


print("INFORMAÇAO CLIENTE")
print(f"Nome cliente: {cliente1.nome}")
print(f"e-mail: {cliente1.email}")
print(f"Telefone: {cliente1.telefone}")
print()
print("==============================")
print()
print("INFORMAÇAO FUNCIONARIO")
print(f"Nome funcionario: {funcionario1.nome}")
print(f"matricula: {funcionario1.matricula}")
print(f"e-mail:{funcionario1.email}")
print(f"setor: {funcionario1.setor}")
