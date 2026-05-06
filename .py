import os 
from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preço: float

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Autor: {self.autor}')
        print(f'Categoria: {self.categoria}')
        print(f"Preço: {self.preço}")

QUANTIDADE_LIVROS = 3
lista_livros = []

print("===SISTEMA DE CADASTRO====")
print("1 == ADICIONAR LIVRO")
print("2 == LISTAR LIVROS")
print("3 == SAIR")
# Transformei a opção em variável para o match processar corretamente
opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        print("Opção 1 selecionada: Adicionar livro")
        print("\n== SOLICITANDO DADOS==")
        for i in range(QUANTIDADE_LIVROS):
            novo_livro = Livro(
                nome=input(f"Digite o nome do seu {i+1}º livro: "),
                autor=input(f"Digite o autor do {i+1}º livro: "),
                categoria=input(f"Digite a categoria do {i+1}º livro: "),
                
                preço=float(input(f"Digite o preço do {i+1}º livro: "))
            )
            lista_livros.append(novo_livro)
            
           
            with open("catalago_livros.csv", "a") as arquivo:
                arquivo.write(f"{novo_livro.nome},{novo_livro.autor},{novo_livro.categoria},{novo_livro.preço}\n")

    case 2:
        print("Opção 2 selecionada: Listar livros")
        # Verificando se o arquivo existe antes de tentar ler
        if os.path.exists("catalago_livros.csv"):
            with open("catalago_livros.csv", "r") as arquivo:
                for linha in arquivo:
                    nome, autor, categoria, preço = linha.strip().split(",")
                    livro_carregado = Livro(nome, autor, categoria, float(preço))
                    livro_carregado.mostrar_dados()
                    print("-" * 20)
        else:
            print("Nenhum livro cadastrado no arquivo.")

    case 3:
        print("Opção 3 selecionada: Sair")

print("FIM")

