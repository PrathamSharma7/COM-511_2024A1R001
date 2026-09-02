'''
Write a python program to take a password and check whether it contains @ and has at least 8 characters
'''

password = input("Enter password: ")
print(f"Has '@'? : {'@' in password}")
print(f"Is at least 8 characters long? : {len(password) >= 8}")