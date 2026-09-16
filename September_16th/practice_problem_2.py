'''
Write a python program to input marks of 10 students. Store only
valid marks between 0 and 100 in a list. Skip invalid marks.
'''

marks = []
for i in range(10):
    mark = int(input(f"Enter marks of student {i+1}: "))
    if 0 <= mark <= 100:
        marks.append(mark)

print("\nValid marks:", end = " ")
for mark in marks:
    print(mark, end = " ")