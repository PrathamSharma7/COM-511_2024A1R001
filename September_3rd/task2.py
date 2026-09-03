'''
Take a roll no like 2024A1R057 and extract admission year, program code and roll number digits using slicing
'''

roll_no = input("Enter roll number: ")
admission_year = roll_no[:4]
program_code = roll_no[4:6]
roll_number_digits = roll_no[7:]

print(f"""Admission Year: {admission_year}
Program Code: {program_code}
Roll Number: {roll_number_digits}""")