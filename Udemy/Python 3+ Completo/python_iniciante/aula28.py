# Aula 28 -> Exercício de fixação

# Função para verificar se há espaços em uma string
def has_space(s: str) -> bool:
    for i in range(len(s)):
        if s[i] == " ":
            return True
    return False

# Função para obter nome e idade do usuário com validação
def initial_loop() -> tuple[str, int]:
    while True:
        name_input:str = input("Enter your full name: ")

        if name_input == "":
            print("You did not enter a name. Please try again.")
            continue
        
        age_input:str = input("Enter your age: ")

        if not age_input.isdigit():
            print("Invalid age. Please enter a numeric value.")
            continue
        
        return name_input, int(age_input)

# Função principal
def main() -> None:
    name, age = initial_loop() # Atribui a tupla devolvida pela função às variáveis name e age

    print(f"\nYour name is: {name}")
    print(f"Your age is: {age}")
    print(f"Your name reversed is: {name[::-1]}")

    if has_space(name):
        print("Your name has spaces")
    else:
        print("Your name has no spaces")
        
    print(f"Your name has: {len(name)} characters")
    print(f"Your first letter is: {name[0]}")
    print(f"Your last letter is: {name[-1]}", end="\n\n")

main()