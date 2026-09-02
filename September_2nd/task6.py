'''
Write a python program to take a word and count the number of vowels 'a,e,i,o,u'
'''

string = input("Enter string: ")
a_count = string.count('a')
e_count = string.count('e')
i_count = string.count('i')
o_count = string.count('o')
u_count = string.count('u')
vowel_count = a_count + e_count + i_count + o_count + u_count

print(f"""Number of a: {a_count}
Number of e: {e_count}
Number of i: {i_count}
Number of o: {o_count}
Number of u: {u_count}
Number of vowels: {vowel_count}""")