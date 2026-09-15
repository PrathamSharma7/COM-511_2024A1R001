'''
Write a Python program to print Floyd's triangle.
1
2 3
4 5 6
7 8 9 10
'''

num = 1
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()