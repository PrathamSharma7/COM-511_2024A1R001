'''
Write a python program to determine whether a student is eligible for a scholarship
The scholarship should be granted if the student satisfies either of the following conditions:
a. The student has a CGPA of 8.5 or above and attendence of 85 or above\
b. The student has won a national-level competition

The program should take CGPA, attendence percentage and national-level-competition status as input,
then display whether the student is eligible for the scholarship
'''

cgpa = float(input("Enter CGPA: "))
attendence = float(input("Enter Attendence: "))
national_level_competition_status = bool(input("Have you won any national level competition: (0 for No, 1 for Yes): "))

is_eligible_for_scholarship = (cgpa >= 8.5 and attendence >= 85) or national_level_competition_status
print("Eligible for scholarship?:",is_eligible_for_scholarship)