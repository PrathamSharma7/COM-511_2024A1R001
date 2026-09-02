'''
Take a sentence containing double spaces and unwanted spaces at beginning or end. clean the sentence
'''
sentence = input("Enter a sentence: ")
sentence = sentence.strip()
sentence = sentence.replace("  ", " ")
print(sentence)