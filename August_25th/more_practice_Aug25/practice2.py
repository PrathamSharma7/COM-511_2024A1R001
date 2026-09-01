# Write a Python program to take marks of three subjects out of 100. Print True if the student scored at least 40 in all three subjects and average marks are at least 50.

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3


print(marks1 >= 40 and marks2 >= 40 and marks3 >= 40 and average >= 50)