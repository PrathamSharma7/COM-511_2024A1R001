'''
Write a Python program to input a number and check whether its prime or not 
'''

n = int(input("Enter a number: "))
for x in range(2, (n//2)+1):
    if not n%x:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")