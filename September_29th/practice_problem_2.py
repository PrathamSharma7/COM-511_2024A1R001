'''
Write a Python program to allocate seats to a group in a single row of a cinema hall.
First, input the total number of seats n. Then, enter the status of each seat:
    1. 0 means the seat is available.
    2. 1 means the seat is already booked.
Next, input the number of people in the group. The program must find the first consecutive block of 
available seats that can accommodate the entire group. If such seats are found:
    1. Book all those seats by changing their status from 0 to 1. 
    2. Display the allocated seat numbers as a tuple.
    3. Display the updated list of seat statuses.
If no such block of seats is found, display "Consecutive seats not available" and print the original seat list without changes.
Conditions:
    1. Seat numbering starts from 1.
    2. The group size must at least 1 and cannot exceed n.
    3. ALl group members must be allotted seats together in consecutive order.
    4. If more than one suitable block is available, allocate the first block from the left.
    5. Input seat status must be either 0 or 1.

Example:
Enter number of seats: 9
Seat Status: [1, 0, 0, 1, 0, 0, 0, 0, 1] 
Enter Group Size: 3

Expected Output:
Allocated Seats: (5,6,7)
Updated Status: [1, 0, 0, 1, 1, 1, 1, 0, 1]
'''

n = int(input("Enter number of seats: "))
seat_status = list(map(int, input("Seat Status: ").split()))
group_size = int(input("Enter Group Size: "))

if group_size < 1 or group_size > n:
    print("Invalid group size")
    exit

for i in range(n - group_size + 1):
    if seat_status[i:i + group_size] == [0] * group_size:
        seat_status[i:i + group_size] = [1] * group_size
        print(f"Allocated Seats: {tuple(range(i + 1, i + group_size + 1))}")
        print(f"Updated Status: {seat_status}")
        break
else:
    print("Consecutive seats not available")