"""
Write a python program to take a word and print it in reverse order using slicing. also check whether the word is same forward and backward
"""
word = input("Enter a word: ")
reversed_word = word[::-1]
print(f"""Word: {word}
Reversed: {reversed_word}
Is Pallindrome? {word.lower() == reversed_word.lower()}""")
