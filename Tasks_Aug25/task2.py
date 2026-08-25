# Write a python Program to take a two digit number as inout and return the sum of its digits

num = int(input("Enter a two digit number: "))
ones_digit = num%10
tens_digit = num//10

sum = ones_digit+tens_digit
print(f"Sum of digits of {num} is {sum}")