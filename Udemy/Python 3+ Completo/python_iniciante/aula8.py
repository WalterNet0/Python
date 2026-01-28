# Aula 8 -> Exercício de Fixação sobre variáveis e tipos de dados

nome:str = input("Digite seu nome: ")
sobrenome:str = input("Digite seu sobrenome: ")

idade:int = int(input("Digite sua idade: "))
ano_atual:int = 2026
ano_nascimento:int = ano_atual - idade
maior_idade:bool = idade >= 18

altura_metros:float = float(input("Digite sua altura em metros (ex: 1.75): "))

print()

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_idade)
print('Altura em metros:', altura_metros, end="\n\n")