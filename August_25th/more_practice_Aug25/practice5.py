'''
 Write a python program to take student  details like name, roll number, CGPA and hostel status from user
 Typecast them into appropriate types and print along with their detected type
'''

name = input("Enter name: ")
roll_no = int(input("Enter Roll No.: "))
cgpa = float(input("Enter CGPA: "))
hostel_status = bool(int(input("Does the student stay in hostel? (0 for No, 1 for Yes): ")))

print(f'''Name: {name}, type: {type(name)}
Roll. No: {roll_no}, type: {type(roll_no)}
CGPA: {cgpa}, type: {type(cgpa)}
Hostel Status: {hostel_status}, type: {type(hostel_status)}''')