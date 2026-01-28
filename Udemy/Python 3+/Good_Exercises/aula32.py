# Aula 32 -> Três exercícios diferentes

import os

# Função para limpar o console
def clear_console() -> None:
    os.system(
        'cls' if os.name ==
        'nt' else 'clear'
    )

# Função para verificar se há espaços em uma string
def has_space(s: str) -> bool:
    for i in range(len(s)):
        if s[i] == " ":
            return True
        
def check_hasNumber(s: str) -> bool:
    for char in s:
        if char.isdigit():
            return True
    return False
        
# Função para perguntar se quer fazer de novo
def ask_repeat() -> bool:
    while True:
        response = input("Do you want to do it again? (yes/no): ").lower().strip()
        if response in ['yes']:
            return True
        elif response in ['no']:
            print()
            return False
        else:
            print("Please type 'yes' or 'no'.", end="\n\n")

# Exercício 1: Verificar se um número é par ou ímpar
def ex1() -> None:
    while True:
        try:
            number:int = int(input("Type a number: "))

            if number % 2 == 0:
                print(f"\nThe number {number} is even.")
                break
            else:
                print(f"\nThe number {number} is odd.")
                break
                
        except ValueError:
            print("Type a integer number.", end="\n\n")

# Exercício 2: Cumprimentar com base na hora do dia
def ex2() -> None:
    while True:
        try:
            hour:int = int(input("Type the hour of the day (0-23): "))

            if 0 <= hour <= 11:
                print("Good morning!")
                break
            elif 12 <= hour <= 17:
                print("Good afternoon!")
                break
            elif 18 <= hour <= 23:
                print("Good evening!")
                break
            else:
                print("The hour must be between 0 and 23.", end="\n\n")
        
        except ValueError:
            print("Type a integer number between 0 and 23.", end="\n\n")

# Exercício 3: Classificar nome do usuário pela quantidade de letras
def ex3() -> None:
    while True:
        name:str = input("Type your first name: ")
        name_length:int = len(name)

        if name == "":
            print("You did not enter a name. Please try again.", end="\n\n")
            continue

        elif check_hasNumber(name):
            print("Names cannot contain numbers. Please try again.", end="\n\n")
            continue

        elif has_space(name):
            print("Please enter only your first name without spaces.", end="\n\n")
            continue

        else:
            if name_length <= 4:
                print(f"\nYour name is short, {name}.")

            elif name_length >= 5 and name_length <= 6:
                print(f"\nYour name is normal, {name}.")

            else:
                print(f"\nYour name is long, {name}.")

            break

# Função principal para selecionar o exercício
def main() -> None:
    while True:
        print("Select the exercise to run:")
        print("[1] Exercise 1\n[2] Exercise 2\n[3] Exercise 3", end="\n\n")

        while True:
            try:
                exercise:int = int(input("Type the exercise number: "))

                if exercise == 1:
                    clear_console()
                    ex1()

                    if not ask_repeat():
                        return
                    
                    clear_console()
                    break   

                elif exercise == 2:
                    clear_console()
                    ex2()

                    if not ask_repeat():
                        return
                    
                    clear_console()
                    break

                elif exercise == 3:
                    clear_console()
                    ex3()

                    if not ask_repeat():
                        return
                    
                    clear_console()
                    break

                else:
                    print("Type a valid exercise number.", end="\n\n")
            except ValueError:
                print("Type a valid integer number between 1 and 3.", end="\n\n")

main()