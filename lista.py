import os 
from dataclasses  import dataclass




@dataclass
class Funcionario:
    nome: str
    idade:int
    def mostra_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")

lista_funcionarios=[]

with open("lista_funcionarios.csv","r") as arquivo:
    for linha in arquivo:
        nome,idade= linha.strip().split(',')
        lista_funcionarios.append(Funcionario(
        nome=nome,
        idade=idade,
        ))
    for funcionario in lista_funcionarios:
        funcionario.mostra_dados()
