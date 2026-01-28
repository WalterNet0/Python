# Aula 14 -> Formatação de strings com o método format()

a = 'AAAAAAA'
b = 'B'
c = 1.1

string = 'a={phrase1} a={phrase1} b={phrase2} c={number:.2f}'

format = string.format(
    phrase1 = a,
    phrase2 = b,
    number = c
) # OBS: format não é palavra reservada do Python

print(format)