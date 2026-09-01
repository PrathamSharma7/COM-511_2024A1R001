'''
Write a python program to take a student's full name and display
-> total number of characters
-> first character
-> last character
-> name in uppercase form 
'''

name = input("Enter name: ")
print(f"Total number of characters: {len(name)}")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Name in uppercase form: {name.upper()}")