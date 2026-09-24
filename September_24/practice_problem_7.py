'''
Write a python program to store multiple student records as list of tuples. Each student must contain name, roll no, marks. display
student who scored above 75
'''

student_data = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll_no = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    student_data.append((name, roll_no, marks))

for student in student_data:
    if student[2] > 75:
        print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}")