'''
Write a python program to create simple password validation system

The password should repeatedly ask the user to enter a password until a valid password is entered.
A password will be considered valid only if it has at least 8 characters and contains the '@' symbol.

Once the user enters a valid password, the program should display "Password Accepted" and stops.
Otherwise it should display "Weak Password. Try Again" and ask for password again.
'''

valid_password = False
while valid_password == False:
    password = input("Enter Password: ")
    if len(password) >= 8 and '@' in password:
        print("Password Accepted")
        valid_password = True
    else:
        print("Weak Password. Try Again")
