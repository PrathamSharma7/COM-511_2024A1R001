'''
Take a student's full name and roll number.
Generate email using the first three letters of first name, first 3 letters of last name and last 3 characters of roll number
'''

full_name = input("Enter full name: ")
first_name, last_name = full_name.split()
roll_no = input("Enter Roll. No.: ")

email = first_name[:3] + last_name[:3] + roll_no[-3:] + "@mietjammu.in"
print(f"Email: {email}")