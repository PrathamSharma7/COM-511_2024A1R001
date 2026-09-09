'''
Write a Python program to detect whther a comment is spam or not. A comment should be treated as spam if it contains
any of these key words: "make a lot of money", "buy this", "subscribe this", or "click this".
'''

comment = input("Enter Comment: ").lower()
spam_keywords = ["make a lot of money", "buy this", "subscribe this", "click this"]
is_spam = False 
for spam_keyword in spam_keywords:
    if spam_keyword in comment:
        print("Comment is spam")
        is_spam = True
        break
else:
    print("Comment is not spam")