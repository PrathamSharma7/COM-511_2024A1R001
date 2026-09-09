'''
Write a python program to take two numbers and find their Greatest Common Divisor using loop
'''

a = int(input("Enter first number: "))
b = int(input("Enter secoond number: "))

# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(f"GCD of {a} and {b} is: {i}")
#         break

# Using Eucledian Algorithm
while b:
    a, b = b, a%b
print(f"GCD: {a}")