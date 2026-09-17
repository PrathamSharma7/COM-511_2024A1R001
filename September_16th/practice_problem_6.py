'''
Write a python program to rotate a list one position to the right
'''

nums = list(map(int, input("Enter a list: ").split()))
nums.insert(0, nums.pop())

print(f"List after rotation: {nums}")