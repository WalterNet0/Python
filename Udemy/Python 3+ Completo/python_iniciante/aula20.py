# Aula 20 -> Exercício de comparação e ordenação de termos

# Linha 8 -> função mais otimizada
# Linha 27 -> função tradicional
# Linha 43 -> função para perguntar se o usuário quer rodar novamente
# Linha 59 -> função main para escolher o exercício

import time as task

# Forma mais otimizada de fazer o exercício
def optional_exercise():
    LIST_SIZE = int(input("How many terms do you want to order? "))

    terms_list:list[float] = []

    for i in range(LIST_SIZE):
        terms_list.append(float(input(f"Type the term number {i + 1}: ")))

    print("\nOrdering the terms...\n")
    task.sleep(2)

    terms_list.sort()

    print("The ordered terms are:")
    for term in terms_list:
        print(term)
    print()

# Forma tradicional de fazer o exercício
def main_exercise():
    number1 = float(input("Type the first number: "))
    number2 = float(input("Type the second number: "))

    print()

    if number1 > number2:
        print(f"{number1} is greater than {number2}\n")
    elif number2 > number1:
        print(f"{number2} is greater than {number1}\n")
    else:
        print("Both numbers are equal\n")

# Função para perguntar se o usuário quer rodar novamente
def ask_to_run_again():
    while True:
        print("Wanna run again?\n")
        choice = input("Type '1' to run again or '2' to exit: ")

        if choice == "1":
            print("\nRunning again...\n")
            return True
        elif choice == "2":
            print("\nExiting the program. Goodbye!\n")
            return False
        else:
            print("\nInvalid choice. Try again.\n")

# Função principal para escolher o exercício
def main():
    while True:
        print("Choose an exercise to run:\n")
        print("1 - Optional Exercise (Ordering Terms)")
        print("2 - Main Exercise (Comparing Numbers)\n")

        choice = input("Type the exercise number (1 or 2): ")

        if choice == "1":
            print("\nYou chose the Optional Exercise.\n")
            optional_exercise()

            if not ask_to_run_again():
                break

        elif choice == "2":
            print("\nYou chose the Main Exercise.\n")
            main_exercise()

            if not ask_to_run_again():
                break

        else:
            print("\nInvalid choice. Please select 1 or 2.\n")

main()