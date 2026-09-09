'''
Write a python Program that asks user to enter a username and password. The user should only get three attempts.
If the correct credentials are entered, display "Login Successful" and stop the loop. 
If all the attempts are used, print Account Locked
'''

correct_username = "admin"
correct_password = 'abc@123'

for i in range(3):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful"); break
    else:
        print("Invalid Credentials, Try Again!!")
else:
    print("Account Locked!")