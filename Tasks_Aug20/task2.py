#Write a python program to calculate Simple Interest and total amount using principal, rate and time entered by user

principal = float(input("Enter Principal: "))
rate_of_interest = float(input("Enter Rate of Interest: "))
time_in_years = int(input("Enter time in years: "))

simple_interest = principal*rate_of_interest*time_in_years
amount = principal + simple_interest
print("Simple Interest:", simple_interest, "\nAmount:",amount)