'''
Write a python program to input marks of 5 students

For each student, the program should check whether the entered marks are valid or invalid.
Marks are considered valid only if they are between 1 and 100. If the marks are invalid, 
the program must display "Invalid Marks Skipped" and move to the next student without printing those marks
'''

marks_1 = int(input("Enter Marks for student 1: "))
marks_2 = int(input("Enter Marks for student 2: "))
marks_3 = int(input("Enter Marks for student 3: "))
marks_4 = int(input("Enter Marks for student 4: "))
marks_5 = int(input("Enter Marks for student 5: "))

if 0 <= marks_1 <= 100:
    print("Marks of Student 1:", marks_1)
else:
    print("Invalid Marks Skipped")
if 0 <= marks_2 <= 100:
    print("Marks of Student 2:", marks_2)
else:
    print("Invalid Marks Skipped")
if 0 <= marks_3 <= 100:
    print("Marks of Student 3:", marks_3)
else:
    print("Invalid Marks Skipped")
if 0 <= marks_4 <= 100:
    print("Marks of Student 4:", marks_4)
else:
    print("Invalid Marks Skipped")
if 0 <= marks_5 <= 100:
    print("Marks of Student 5:", marks_5)
else:
    print("Invalid Marks Skipped")