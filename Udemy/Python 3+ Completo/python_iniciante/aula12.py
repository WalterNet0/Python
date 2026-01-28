# Aula 12 -> Calculadora de IMC (Índice de Massa Corporal)

import time as task

name:str = input("Type your name: ")
weight:float = float(input("Type your weight (kg): "))
height:float = float(input("Type your height (m): "))

bmi = weight / (height ** 2)

print("")
print("Calculating your BMI...", end="\n\n")
task.sleep(2)

print(f"Hello, {name}!")
task.sleep(0.5)

print(f"Your weight: {weight}kg")
print(f"Your height: {height}m", end="\n\n")
task.sleep(1)

print(f"Your BMI is: {bmi:.2f}")