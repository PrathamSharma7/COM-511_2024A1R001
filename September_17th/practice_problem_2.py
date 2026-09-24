'''
Write a python program to store all month names in a tuple, 
input each month number and display the corresponding month name
'''

months = ("January", 
          "February", 
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December")

month_number = int(input("Enter a number for month: "))
if 1 <= month_number <= 12:
    print(f"{month_number}: {months[month_number-1]}")
else:
    print("Invalid Month")