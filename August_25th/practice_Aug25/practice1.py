# Write a python program to take two inputs a and b, swap their values using a temporary variable, and print the updated values.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

temp = a
a = b
b = temp

print(f"Swapped values: \na = {a}\nb = {b}")