'''
Write a python program to take 10 digit mobile number and display only the last 4 digits. Replace the first 6 digits with *******
'''
mobile_number = input("Enter 10 digit mobile number: ")
starred_number = '*' * 6 + mobile_number[-4:]
print(f"Mobile number: {starred_number}")