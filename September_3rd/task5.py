'''
Take a password and check length, presence of @ and whether first and last characters are different
'''

password = input("Enter Password: ")
print(f"""Length: {len(password)}
Has '@'?: {'@' in password}
First and last characters same?: {password[0] == password[-1]}""")