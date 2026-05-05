import os
from dataclasses import dataclass

@dataclass
class Empresa:
    nome:str
    cnpj:str
    telefone:str

    def mostra_dados(self):
        print(f"nome: {self.nome}")
        print(f"cnpj: {self.cnpj}")
        print(f"telefone: {self.telefone}")

lista_empresa=[]

with open("contato_empresa.csv","r") as arquivo:
    for linha in arquivo:
        nome,cnpj,telefone= linha.strip().split(',')
        lista_empresa.append(Empresa(
        nome=nome,
        cnpj=cnpj,
        telefone=telefone))
    for empresa in lista_empresa:
        empresa.mostra_dados()
