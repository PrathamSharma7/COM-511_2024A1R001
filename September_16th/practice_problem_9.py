'''
Write a Python program, to input two lists and create a third list containing common elements.
'''

list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))
common_elements = []

for num in list1:
    if num in list2 and num not in common_elements:
        common_elements.append(num)

print("Common elements:", common_elements)