import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    idade:int

    def mostrar_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}\n")

QUANTIDADE_FUNCIONARIOS = 2
lista_funcionarios=[]

print('- solicitando dados-')
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionario(
        nome=input("digite seu nome: "),
        idade= int(input('digite sua idade: '))
    )
    print("")
    lista_funcionarios.append(novo_funcionario)

print('-EXIBINDO DADOS-')
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

print('salvando dados')
with open("lista_funcionarios.csv","a", encoding= "utf-8") as arquivo:
    for funcionario in lista_funcionarios:
        arquivo.write(f"{funcionario.nome}, {funcionario.idade}\n")
    print("salvo com sucesso!!")

print("= FIM DO PROGRAMA =")