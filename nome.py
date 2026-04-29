import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class pessoa:

    nome:str
    idade:int

@dataclass
class pet:

    nome: str
    idade:int

pessoa1= pessoa("alice",30)
pessoa2=pessoa("renner",40)

pet1=pet("toto",5)
pet2=pet("lucas",6)

print("""
            PET SHOP DO BICO""")
print(f"Nome: {pessoa1.nome}\nIdade:{pessoa1.idade}")
print(f"Nome: {pessoa2.nome}\nIdade:{pessoa2.idade}")
print()
print(f"Nome pet: {pet1.nome}\nIdade: {pet1.idade}")
print(f"Nome pet: {pet2.nome}\nIdade: {pet2.idade}")
