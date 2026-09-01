"""
Write a python program to take an email address and print domain name
"""

email = input("Enter email address: ")
list = email.split("@")
print(f"Domain name: {list[1]}")