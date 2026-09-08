'''
Write a python program to input four numbers from the user and find the greatest number among them
'''

nums = list(map(int, input("Enter 4 Numbers: ").split()))
print("Greatest out of the four numbers:", max(nums))