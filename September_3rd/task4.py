'''
Take name, branch, and year. Generate a code  name using string concatination, slicing and repetition
'''
name = input("Enter Name: ")
branch = input("Enter branch: ")
year = input("Enter year: ")

code_name = name[-3:] + branch + year[-2:]*2
print("Code name:", code_name)