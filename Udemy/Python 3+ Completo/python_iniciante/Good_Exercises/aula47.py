# Aula 47 - Secret word

import random
import time

# Função para retornar o quanto da palavra foi descoberto, e a quantidade de tentativas totais até o momento
def show_status(discovered:list[str], attempts:int, errors:int, showErrors:bool) -> None:
    print("\nWord:", " ".join(discovered))
    print(f"Attempts: {attempts}")

    if showErrors:
        print(f"Errors: {errors}")

    print("")

# Função principal
def main() -> None:
    # Lista com palavras
    secret_words:list[str] = ["Banana", "Dog", "Computer", "Water", "House"]
    secret_word:str = random.choice(secret_words).lower()

    # Declarando e inicializando as variáveis
    discovered:list[str] = ["_"] * len(secret_word) # Lista contendo o tamanho da palavra, preenchida por "_", inicialmente
    used_letters:set[str] = set() # Collection contendo palavras já utilizadas anteriomente

    # Tentativas e erros totais
    attempts:int = 0
    errors:int = 0

    # Enquanto a palavra não foi descoberta
    while "_" in discovered:
        char:str = input("Type a char: ").lower()

        # Verificações
        if not char:
            print("You must type a letter.", end="\n\n")
            continue

        if len(char) > 1:
            print("Type a letter only.", end="\n\n")
            continue

        if char.isdigit():
            print("Numbers are not allowed.", end="\n\n")
            continue

        if not char.isalpha():
            print("Only letters are allowed.", end="\n\n")
            continue

        if char in used_letters:
            print("\nYou already used this letter")
            print(f"Used letters:", ", ".join(sorted(used_letters)), end="\n\n") # Devolve a Collection contendo os chars utilizados

            continue
        
        # Caso não tenha sido usada ainda, adiciona à lista, e aumenta a quantidade total de tentativas
        used_letters.add(char)
        attempts += 1

        # Caso char esteja em secret_word, irá preencher seu espaço na lista discovered, na sua respectiva posição no lugar de "_"
        if char in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == char:
                    discovered[i] = char
            show_status(discovered, attempts, errors, showErrors = False)

        else:
            print("\nLetter not in word.")
            errors += 1

            show_status(discovered, attempts, errors, showErrors = True)
            
    # Somente um loading
    print("Loading your stats...", end="\n\n")
    time.sleep(2)
        
    # Stats do player
    print("You guessed the word!")
    print(f"Total attempts: {attempts}")
    print(f"Total errors: {errors}")
    print(f"The secret word is: {secret_word.capitalize()}", end="\n\n") # secret_word.capitalize() irá imprimir a palavra, porém com o primeiro caractere maiúsculo

main()