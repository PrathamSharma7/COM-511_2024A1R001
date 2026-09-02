'''
Write a python program to take a string and seperate characters present at even index positions  and odd index positions
'''

string = input("Enter a string: ")
even_indexed_characters = string[::2]
odd_indexed_characters = string[1::2]

print("Characters at even indexes:", even_indexed_characters)
print("Characters at odd indexes:", odd_indexed_characters)