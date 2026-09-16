'''
Write a python program to input marks of n students in a list.
Display highest marks, average marks and number of student who passed (Assuming passed marks >= 30).
'''

n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    mark = int(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)

highest_marks = max(marks)
average_marks = sum(marks) / n
passed_students = 0
for mark in marks:
    if mark >= 30:
        passed_students += 1

print(f"Highest marks: {highest_marks}")
print(f"Average marks: {average_marks}")
print(f"Number of passed students: {passed_students}")