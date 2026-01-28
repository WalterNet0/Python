# Aula 6 -> Casting

w1:str = "10"

print(f"Value of w1: {w1}")
print(f"Type of w1: {type(w1)}", end="\n\n")

# Casting w1 from str to float
w1 = float(w1)

print(f"Value of w1 after casting to float: {w1}")
print(f"Type of w1 after casting to float: {type(w1)}", end="\n\n")

# Casting w1 from float to bool
w1 = bool(w1)

print(f"Value of w1 after casting to bool: {w1}")
print(f"Type of w1 after casting to bool: {type(w1)}", end="\n\n")

print(f"Printing empty string casted to bool: {bool('')}")
print(f"Printing space string casted to bool: {bool(' ')}", end="\n\n")