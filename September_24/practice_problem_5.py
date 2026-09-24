'''
Write a Python program to check whether a given value is present in a tuple. If yes, display the position
'''

t = tuple(map(int, input("Enter values: ").split()))
target = int(input("Enter value to check: "))
if target in t:
    print(f"{target} is present in the tuple at position {t.index(target)}.")
else:
    print(f"{target} is not present in the tuple.")