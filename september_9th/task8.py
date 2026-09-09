'''
Write a Python Program to repeatedly calculate sum of digits of a number until result becomes a single digit
'''

n = int(input("Enter a Number: "))

while n//10:
    # code to calculate sum of all numbers
    sum = 0
    while n:
        rem = n%10
        sum += rem
        n//=10
    n = sum

print("Single digit sum: ", n)