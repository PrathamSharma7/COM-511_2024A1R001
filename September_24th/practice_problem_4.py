'''
Write a python program to store repeated values in a tuple and count how many times a given value appears.
'''

t = tuple(map(int, input("Enter values: ").split()))
target = int(input("Enter value to count: "))
count = t.count(target)
print(f"{target} appears {count} times in the tuple.")