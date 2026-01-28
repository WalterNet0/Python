# Aula 29 -> Exceções

while True:
    try:
        number = float(input("I'll double any number you give me. Please enter a number: "))
        print(f"The double of {number} is {number * 2}", end="\n\n")
        break
    except ValueError:
        print("That's not a valid number. Please enter a numeric value.", end="\n\n")