import os 
from dataclasses import dataclass

@dataclass
class Livro:
    nome:str
    autor:str
    categoria:str
    preço:float

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'autor: {self.autor}')
        print(f'categoria: {self.categoria}')
        print(f"preço: {self.preço}")

QUANTIDADE_LIVROS =3
lista_livros=[]

print("===SISTEMA DE CADASTRO====")
print("1== ADICIONAR LIVRO===")
print("2==LISTA LIVORS===")
print("3=== SAIR===")

match  int(input("digite a opçao desejada:")):

    case 1:
        print("opçao 1 selecionada adicionar livro")
    case 2:
        print("opiçao 2 selecionar: lista liros")
    case 3:
        print("opiçao 3 selecionada: sair")

        print("\n == SOLICITANDO DADOS==")
for i in  range (QUANTIDADE_LIVROS):
    novo_livro= Livro(
    nome= input(f"digite o nome do seu {i+1} livro:"),
    autor=input(f"digite o autor do {i+1}  livro:"),
    categoria=input(f"digite a categoria do {i+1}  livro:"),
    preço=input(f"digite o preço do {i+1}  livro:")
    )

with open("catalago_livros.csv","r") as arquivo:
    for linha in  arquivo:
        nome,autor,categoria,preço=linha.strip().split(",")
        lista_livros.append(Livro(
            nome=nome,
            autor=autor,
            categoria=categoria,
            preço=preço

        ))
    print("FIM")