# Aula 27 -> Fatiamento de Strings em Python e a função len()

phrase:str = "Python 3 course from beginners to advanced"

print("Printing the entire string:", end="\n\n")

print(f"Using 'print(phrase)': {phrase}")  # Saída: Python 3 course from beginners to advanced
print(f"Using 'print(phrase[:])': {phrase[:]}") # Saída: Python 3 course from beginners to advanced
print(f"Using 'print(phrase[0:len(phrase):1])': {phrase[0:len(phrase):1]}", end="\n\n") # Saída: Python 3 course from beginners to advanced

print("Printing specific parts of the string:", end="\n\n")
print(f"Using 'print(phrase[:15])': {phrase[:15]}") # Saída: Python 3 course
print(f"Using 'print(phrase[16:])': {phrase[16:]}", end="\n\n") # Saída: from beginners to advanced
print("Printing skipping characters with a step value:", end="\n\n")
print(f"Using 'print(phrase[0:len(phrase):2])': {phrase[0:len(phrase):2]}") # Saída: Pto  orefo einr oavne
print(f"Using 'print(phrase[::2])': {phrase[::2]}", end="\n\n") # Saída: Pto  orefo einr oavne

print("Reversing the string using negative step value:", end="\n\n")
print(f"Using 'print(phrase[::-1])': {phrase[::-1]}") # Saída: decnavda ot srennigeb morf esruoc 3 nohtyP
print(f"Using 'print(phrase[-8:])': {phrase[-8:]}", end="\n\n") # Saída: advanced