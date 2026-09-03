'''
Take an email address and print username, domain and reversed domain
'''

email = input("Enter Email: ")
username, domain = email.split('@')
print(f"""Username: {username}
Domain: {domain}
Reversed Domain: {domain[::-1]}""")