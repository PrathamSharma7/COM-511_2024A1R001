"""Write a python program to take a student name and roll number, then generate a username using the 
first three letters of the name and last 2 digits of the roll number.
"""

name = input("Enter name: ")
roll_no = input("Enter Roll No.: ")

username = name[:3] + roll_no[-2:]

print(f"Username: {username}")