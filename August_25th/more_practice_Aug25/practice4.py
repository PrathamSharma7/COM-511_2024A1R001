# Write a Python program to take input from the user without typecasting and multiply by 3. Then typecast the same input to int and multiply by 3. Print both results to show the difference

num = input("Enter a number: ")
print(f"Without Typecasting: {num*3}")

typecasted_num = int(num)
print(f"With Typecasting: {typecasted_num*3}")