'''
Write a python program to input a number and reverse it using arithematic operations only
'''

n = int(input("Enter a Number: "))
temp = n
reverse = 0
while n:
    rem = n%10
    reverse = reverse * 10 + rem
    n//=10

print(f"Original: {temp}, Reversed: {reverse}")