'''
Create a class and object: Student Details
Problem: Create a student class to store a student's name and roll number.
Create an object and display the details using an instance method
'''

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    #instance_method
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

student_1 = Student("Alex", 1001)
student_2 = Student("Bob", 1002)

student_1.show_details()
student_2.show_details()