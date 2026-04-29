import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Fornecedor:
    nome:str
    email:str
    telefone:int
    endereço:int

print("\n==solicitando dados==")
fornecedor=Fornecedor(
    nome=input("digite o nome do fornecedor:"),
    email=input("digite seu email:"),
    telefone=input("digite o telefone:"),
    endereço=input("digite o enderenço:")

)

os.system("cls")
print("\n== dados do fornecedor==")
print(f"nome:{fornecedor.nome}")
print(f"idade:{fornecedor.email}")
print(f"telefone:{fornecedor.telefone}")
print(f"endereço:{fornecedor.endereço}")




