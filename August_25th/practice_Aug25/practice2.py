# Write a python program to swap two numbers without using a third variable (Use arithmetic operators)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a = a + b
b = a - b
a = a - b
print(f"Swapped values: \na = {a}\nb = {b}")