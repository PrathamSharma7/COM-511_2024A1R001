# Write a python program to take an amount in ruppees and calculate how many Rs 500 and Rs 100 notes are needed

amount = int(input("Enter Amount: "))
five_hundred_notes = amount//500
amount%=500
hundred_notes = amount//100

print(f"Number of Rs 500 Notes: {five_hundred_notes}\nNumber of Rs 100 Notes: {hundred_notes}")