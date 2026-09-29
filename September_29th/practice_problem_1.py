'''
Write a Python program to input a student's marks in a  consecutive tests and store them in a list.
Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.

Display the sequence, its length, and its starting and ending test numbers in a tuple. If multiple sequences have the same 
maximum length, display the first one.

Marks: [55,60,68,62,65,70,78,74]
Longest improving sequence: (62, 65, 70, 78)
Number of test: 4
Test Range: (4, 7)

Conditions:
1. Accept at least 1 test
2. Equal marks break the improving sequence.
3. Test numbers begin at 1
4. Do not sort the list, the original test order matters.
''' 

marks = list(map(int, input("Enter the student's marks: ").split()))

starting_index = ending_index = 0
max_length = 0
current_length = 1

for i in range(1, len(marks)):
    if marks[i] > marks[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            starting_index = i - current_length
            ending_index = i - 1
        current_length = 1

# Check at the end of the loop in case the longest sequence is at the end of the list
if current_length > max_length:
    max_length = current_length
    starting_index = len(marks) - current_length
    ending_index = len(marks) - 1

print("Longest improving sequence:", tuple(marks[starting_index:ending_index + 1]))
print("Number of tests:", max_length)
print("Test Range:", (starting_index + 1, ending_index + 1))