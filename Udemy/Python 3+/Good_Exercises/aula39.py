# Aula 39 -> Exercício para misturar símbolos a uma string

import os

# Função para limpar o console
def clear_console() -> None:
    os.system(
        'cls' if os.name ==
        'nt' else 'clear'
    )

# Função para verificar se a string contém números
def check_hasNumber(s: str) -> bool:
    for char in s:
        if char.isdigit():
            return True
    return False

# Função para misturar símbolos com o nome
def mix_symbols(name: str, symbols: str) -> str:
    mixed:str = f"{symbols}" # Começa com o símbolo

    for i in range(len(name)):
        mixed += f"{name[i]}{symbols}"

    return mixed

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

# Função principal
def main() -> None:
    name:str = ""
    symbols:str = ""

    while True:
        name = input("Type a name: ")

        if check_hasNumber(name):
            print("The name cannot contain numbers.", end="\n\n")
            continue

        symbols = input("Type a symbol: ")

        print(f"\nNormal name: {name}")
        print(f"Name mixed with the symbols: {mix_symbols(name, symbols)}", end="\n\n")

        if not ask_repeat():
            break

        clear_console()

main()