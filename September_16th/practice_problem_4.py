'''
Write a Python Program to input a list of numbers and create a new list containing only unique elements
'''

nums = list(map(int, input("Enter a list: ").split()))
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(f"List with unique elements: {unique_nums}")