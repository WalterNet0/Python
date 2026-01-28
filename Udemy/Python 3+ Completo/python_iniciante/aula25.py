#  Aula 25 -> Interpolação com de strings com %

import time as task

name:str = input("Type your name: ")

fruitsList:list[str] = ["Apple", "Banana", "Cherry", "Pear", "Elderberry"]

print("\nHello, %s! Loading the fruits in your list:" % name, end="\n\n")
task.sleep(2)

for fruit in fruitsList:
    print(fruit)