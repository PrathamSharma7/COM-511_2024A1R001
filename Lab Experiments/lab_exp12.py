'''
Create a function max_of_three that takes three numbers as arguments and returns the largest of them 
and also create a parameter function that checks whether a given number is Armstrong or not. 
'''
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def is_armstrong(n):
    temp = n
    digits = 0
    total = 0

    # Count the number of digits
    while temp > 0:
        digits += 1
        temp //= 10

    temp = n

    # Calculate the sum of digits raised to the power
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest number:", max_of_three(a, b, c))

n = int(input("Enter a number: "))


if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")