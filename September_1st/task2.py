"""
Write a Python program to fill the given letter template with name and date.
letter = '''
Dear <Name>,
You are selected!
<Date>
'''
"""

name = input("Enter Name: ")
date = input("Enter Date: ")
letter = f'''Dear {name},
You are Selected!
{date}'''
print(letter)