import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome:str
    email:str
    telefone:int

print("== solicitando dados do cliente==")
cliente=Cliente(
    nome=input('digite seu nome:'),
    email=input('digite seu email:'),
    telefone=input('digite seu telefone:')
)
os.system("cls")
print('\n== exibindo dados do cliente==')
print(f"nome: {cliente.nome}")
print(f"e-mail: {cliente.email}")
print(f"Telefone: {cliente.telefone}")
