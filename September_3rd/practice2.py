'''
Write a python program to simulate a digital lock system

The lock should ask user to enter a 4-digit pin. If the enetered pin does not contain exactly 4 digits,
the program should display an error message and ask again. If the entered PIN is correct the lock should 
open. Otherwise, the program should ask user to try again.
'''

original_pin = 1234
while True:
    pin = int(input("Enter PIN: "))
    if len(str(pin)) != 4:
        print("PIN must contain 4 digits. Please try again!")
    elif pin == original_pin:
        print("UNLOCKED!"); break
    else:
        print("Wrong pin. Please try again!")