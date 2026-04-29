import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class paciente:
    nome:str
    idade:str
    peso:str
    altura:str

print("== solicitando dados do cliente==")
paciente=paciente(
    nome=input('digite seu nome:'),
    idade=input('digite sua idade:'),
    peso=input('digite seu peso:'),
    altura=input('digite sua altura:')
)
os.system("cls")
print('\n== exibindo dados do cliente==')
print(f"nome: {paciente.nome}")
print(f"idade: {paciente.idade}")
print(f"peso: {paciente.peso}")
print(f"altura: {paciente.altura}")