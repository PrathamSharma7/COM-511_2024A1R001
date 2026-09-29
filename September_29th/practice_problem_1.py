'''
Write a Python program to input a student's marks in a  consecutive tests and store them in a list.
Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.

Display the sequence, its length, and its starting and ending test numbers in a tuple. If multiple sequences have the same 
maximum length, display the first one.

Marks: [55,60,68,62,65,70,78,74]
Longest improving sequence: (62, 65, 70, 78)
Number of test: 4
Test Range: (4, 7)
'''

marks = []
n = int(input("Enter number of tests: "))
for i in range(n):
    mark = int(input(f"Enter marks for test {i + 1}: "))
    marks.append(mark)

starting_index = ending_index = 0
