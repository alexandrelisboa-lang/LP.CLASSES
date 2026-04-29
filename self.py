import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome:str
    email:str
    telefone:int

    def mostra_dados(self):
        
        print(f"nome: {self.nome}")
        print(f"e-mail: {self.email}")
        print(f"Telefone: {self.telefone}")


print("== solicitando dados do cliente==")
cliente=Cliente(
    nome=input('digite seu nome:'),
    email=input('digite seu email:'),
    telefone=input('digite seu telefone:')
)
print('\n== exibindo dados do cliente==')
cliente.mostra_dados()

