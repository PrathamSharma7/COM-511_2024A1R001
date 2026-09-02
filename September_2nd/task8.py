"""
Write a python program to take a sentence, detect double spaces, and replace them with single spaces
"""

sentence = input("Enter a sentence: ")
print("double spaces found at:", sentence.find("  "))
sentence = sentence.replace("  ", " ")
print(f"Sentence with single spaces only:\n{sentence}") 