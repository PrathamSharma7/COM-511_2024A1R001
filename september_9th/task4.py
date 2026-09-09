'''
Write a python function to check whether a number is a perfect number.
A number is perfect if the sum of its proper divisors equal to the number itself
'''

n = int(input("Enter a Number: "))
sum = 0
for x in range(1,n//2 + 1):
    if not n%x:
        sum+=x

if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")