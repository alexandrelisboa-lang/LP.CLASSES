import os 
os.system("cls")

from dataclasses import dataclass

@dataclass
class Empresa:
    nome:str
    cnpj:str
    telefone:int

    def mostra_dados(self):
        print(f"nome: {self.nome}")
        print(f"cnpj: {self.cnpj}")
        print(f"telefone: {self.telefone}")

dados_Empresa = []
print("=solicitando dados=")
for i in range(1):
    
    nova_empresa = Empresa(
    nome= input("digite o nome da sua empresa:"),
    cnpj= int(input("digite o cnpj da sua empresa:")),
    telefone=int(input("digite o telefone da sua empresa:"))
    )
    print("")
    dados_Empresa.append(nova_empresa)

    print("=EXIBINDO DADOS=")
    for Empresa in dados_Empresa:
        Empresa.mostra_dados()
    
    print("=SALVANDO DADOS=")
    with open("contato_empresa.csv","a",encoding="utf-8") as arquivo:
        for Empresa in dados_Empresa:
            arquivo.write(f"{Empresa.nome}, {Empresa.cnpj}, {Empresa.telefone}\n")

        print("salvo com sucesso!!")

print("= FIM DO PROGRAMA =")

