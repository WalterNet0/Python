# Aula 4 -> Int e Float

value1 = 10
value2 = 20

value3 = 10.0
value4 = 20.0

comparison1 = type(value1) == type(value3)
comparison2 = type(value2) == type(value4)

print("Variables values:")
print(f"value1: {value1}, value2: {value2}")
print(f"value3: {value3}, value4: {value4}", end="\n\n")

print(f"Type of value1: {type(value1)}")
print(f"Type of value2: {type(value2)}")
print(f"Type of value3: {type(value3)}")
print(f"Type of value4: {type(value4)}", end="\n\n")

print(f"Types Comparison 1 (value1 vs value3): {comparison1}")
print(f"Types Comparison 2 (value2 vs value4): {comparison2}", end="\n\n")

print(f"Values Comparison 1 (value1 vs value3): {value1 == value3}")
print(f"Values Comparison 2 (value2 vs value4): {value2 == value4}", end="\n\n")