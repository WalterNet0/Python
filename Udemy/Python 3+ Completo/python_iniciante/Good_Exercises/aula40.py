# Aula 40 -> Calculadora

import os

# Função para limpar o console
def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para checar se o operador passado realmente é um operador
def check_operator(operator: str) -> bool:
    valid_operators: list[str] = ['+', '-', '*', '/', '//', '%', '**']

    if operator not in valid_operators:
        print(f"Invalid operator. Choose one of: {valid_operators}", end="\n\n")

    return operator in valid_operators

# Função para calcular baseado no operador
def calculate(n1: float, n2: float, op: str) -> float:
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '//':
        return n1 // n2
    elif op == '%':
        return n1 % n2
    elif op == '**':
        return n1 ** n2

# Função principal do programa
def main() -> None:
    number1: float = 0.0
    number1: float = 0.0
    operator: str = ""
    result: float = None

    print("Calculator")
    print("Type 'yes' to quit after a calculation.\n")

    while True:
        # Imprime o resultado atual
        print(f"Actual result: {result}", end="\n\n")

        # Número 1
        if result is None: # Caso já tenha feito um cálculo, result != None, logo não perguntará number1 de novo
            while True:
                try:
                    number1 = float(input("First number: "))
                    print(number1, end="\n\n")
                
                    break

                except ValueError:
                    print("Invalid number. Try again.\n")

        else: # Senão, irá atribuir number1 como o previous result
            number1 = result
        
        # Operador
        operator = input("Operator (+ - * / // % **): ")

        # Checa se o operador passado realmente é um operador válido, até ser digitado um válido
        while not check_operator(operator):
            operator = input("Operator (+ - * / // % **): ")

        print(f"{number1} {operator}", end="\n\n")

        # Número 2
        while True:
            try:
                number2 = float(input("Second number: "))
            
                if operator in ['/', '//', '%'] and number2 == 0: # Caso tente qualquer divisão por 0, não será permitido
                    print("Division by zero is not allowed.\n")
                    continue

                print(f"{number1} {operator} {number2}", end="\n\n")
                break

            except ValueError:
                print("Invalid number. Try again.\n")

        # Calculando resultado baseado no operador
        result = calculate(number1, number2, operator)

        # Printando o resultado
        print(f"Result: {result}\n")

        option = input("Wanna quit? (yes/no): ").lower()
        if option == "yes":
            break

        # Limpa o console após digitar 'no'
        clear_console()

main()