'''
Write a Python program to input a list and create two seperate lists for 
even and odd numbers
'''

nums = list(map(int, input("Enter a list: ").split()))
even_nums = []
odd_nums = []

for num in nums:
    if num % 2:
        odd_nums.append(num)
    else:
        even_nums.append(num)

print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")