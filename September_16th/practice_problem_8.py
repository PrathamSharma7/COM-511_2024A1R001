'''
Write a Python program to count how many times a particular element appears in a list
'''

l = list(map(int, input("Enter a list: ").split()))
target = int(input("Enter the element to count: "))

# print(f"{target} appears {l.count(target)} times in the list.")

count = 0
for item in l:
    if item == target:
        count += 1

print(f"{target} appears {count} times in the list.")