# Write a Python program to take total minutes as input and convert it into hours and remaining minutes

total_minutes = int(input("Enter total minutes: "))
hours = total_minutes//60
minutes = total_minutes%60

print(f"Hours: {hours}\nMinutes: {minutes}")