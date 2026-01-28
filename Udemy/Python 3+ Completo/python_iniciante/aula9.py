# Aula 9 -> Operadores Aritméticos

# Operadores Aritméticos
sum = (f"10 + 5 = {10 + 5}")
subtraction = (f"10 - 5 = {10 - 5}")
multiplication = (f"10 * 5 = {10 * 5}")

division = (f"10 / 4 = {10 / 4}") # Sempre retorna float
floor_division1 = (f"10 // 3 = {10 // 3}") # Retorna o valor inteiro da divisão
floor_division2 = (f"10 // 2 = {10 // 2}") # Retorna o valor inteiro da divisão

exponentiation = (f"2 ** 3 = {2 ** 3}") # 2 elevado a 3
modulus1 = (f"10 % 3 = {10 % 3}") # Resto da divisão -> 1
modulus2 = (f"10 % 2 = {10 % 2}") # Resto da divisão -> 0

print("Operadores Aritméticos:")

print(f"Sum: {sum}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division1}")
print(f"Floor Division: {floor_division2}")
print(f"Exponentiation: {exponentiation}")
print(f"Modulus1: {modulus1}")
print(f"Modulus2: {modulus2}", end="\n\n")

print(f"Is 10/2 even? {10 % 2 == 0}") # Verifica se o número é par
print(f"Is 10/3 odd? {10 % 3 != 0}", end="\n\n") # Verifica se o número é ímpar