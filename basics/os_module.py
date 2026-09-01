# """
# Write a python program to print the contents of a directory using the 
# os module.
# """
import os
# # result = os.listdir()
# # print(result)
# """
# this_directory= os.getcwd()
# print(this_directory)
# """
# """
# os.mkdir("NEW_DIRECTORY")
# print(os.path.exists("NEW_DIRECTORY"))
# print(os.path.exists("NOT_DIRECTORY"))
# """
# os.rename("text.txt","new_text.txt")
# os.rename("old_folder","new_folder")

print(os.path.isfile("dummy1.py"))
print(os.path.isfile("new_folder"))
print(os.path.isdir("dummy1.py"))
print(os.path.isdir("new_folder"))
os.remove('new_text.txt')
os.rmdir('NEW_DIRECTORY')