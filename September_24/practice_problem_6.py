'''
Write a Python program to store one student data as tuple: name, roll no and marks. Display grade based on marks
'''

name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

student_data = (name, roll_no, marks)

student_marks = student_data[2]
if student_marks >= 90:
    grade = 'A'
elif student_marks >= 75:
    grade = 'B'
elif student_marks >= 60:
    grade = 'C'
else:
    grade = 'F'

print(f"Student Name: {student_data[0]}")
print(f"Roll Number: {student_data[1]}")
print(f"Marks: {student_data[2]}")
print(f"Grade: {grade}")