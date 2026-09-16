'''
Write a python program to rotate a list one position to the right
'''

nums = list(map(int, input("Enter a list: ").split()))
last_element = nums[-1]
nums.insert(0, last_element)
nums.pop()

print(f"List after rotation: {nums}")