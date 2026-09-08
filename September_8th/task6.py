'''
Write a python program to input four numbers from the user and find the greatest number among them
'''
max = float('-inf')
for i in range(4):
    num = int(input("Enter number: "))
    if num > max:
        max = num

print("Greatest number enetered:", max)