'''
Problem 2 Library Reservation Queue
Create a Book class that stores the available copies of one textbook and its waiting queue. Implement request(student_id) and return_copies(quantity). For a request, lend one copy if available. Otherwise, add the student to the end of the queue. On a return, add the copies and immediately lend them to waiting students in queue order until there are no waiting students or no copies left. Count all loans made during the simulation, including loans made from returned copies.
Input format: Line 1 contains the initial copy count. Line 2 contains the number of operations N. The next N lines contain REQUEST student_id or RETURN quantity.
Output format: Print available_copies total_loans on line 1. On line 2, print the waiting IDs in queue order, separated by spaces, or EMPTY.
Constraints: Initial copies are between 0 and 50. 1 ≤ N ≤ 100. Return quantities are between 1 and 50. Each student ID is a single token and appears in at most one request. Returns may include copies lent before the simulation.
'''

class Book:
    def __init__(self, initial_copies):
        self.available_copies = initial_copies
        self.waiting_queue = []
        self.total_loans = 0

    def request(self, student_id):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.total_loans += 1
        else:
            self.waiting_queue.append(student_id)

    def return_copies(self, quantity):
        self.available_copies += quantity
        while self.waiting_queue and self.available_copies > 0:
            self.waiting_queue.pop(0)
            self.available_copies -= 1
            self.total_loans += 1

initial_copies = int(input())
book = Book(initial_copies)
n = int(input())

for i in range(n):
    line = input().split()
    if line[0] == "REQUEST":
        book.request(line[1])
    else:
        book.return_copies(int(line[1]))


print("\nOUTPUT\n")
print(book.available_copies, book.total_loans)
if book.waiting_queue:
    print(' '.join(book.waiting_queue))
else:
    print("EMPTY")
