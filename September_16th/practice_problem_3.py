'''
Write a python program to input numbers in a list and find the second largest number.
'''

nums = list(map(int, input("Enter numbers: ").split()))
largest = second_largest = float('-inf')

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print(f"Second Largest Number: ", second_largest)