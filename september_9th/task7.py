'''
Write a Python Program to print numbers from 1 to 50 and skip all those divisible by 4
'''

for i in range(1,51):
    if i%4 == 0:
        continue
    print(i, end = " ")