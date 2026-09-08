'''
Write a python program to input marks of 5 students

For each student, the program should check whether the entered marks are valid or invalid.
Marks are considered valid only if they are between 1 and 100. If the marks are invalid, 
the program must display "Invalid Marks Skipped" and move to the next student without printing those marks
'''

for i in range(1,6):
    marks = int(input("Enter marks: "))

    if 0 <= marks <= 100:
        print("Valid Marks:", marks)
    else:
        print("Invalid Marks Skipped")
        