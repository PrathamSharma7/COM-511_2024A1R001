'''
Write a Python program to input a decimal number and convert it into binary without using the built-in bin() function
'''

n = int(input("Enter a Decimal Number: "))
binary = ""
while n:
    rem = n % 2
    binary = str(rem) + binary
    n //= 2

print(f"Binary Number: {binary}")