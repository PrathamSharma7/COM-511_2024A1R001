'''
Problem 1 Campus Helpdesk Ticket Report
The campus IT helpdesk logs ticket status updates. A lab code and ticket ID together identify one ticket.
Convert lab codes to uppercase, then keep only the last status recorded for each ticket. Count tickets whose final status is OPEN in each lab. List only labs with open tickets. Sort by decreasing count and break ties alphabetically by lab code.
Input format: Line 1 contains the number of updates N. Each of the next N lines contains lab_code ticket_id status. Status is OPEN or CLOSED.
Output format Print LAB_CODE count on one line per qualifying lab. If every ticket is closed, print NO OPEN TICKETS.
Constraints 1 ≤ N ≤ 100. Lab codes and ticket IDs are single tokens of 1–20 characters. Ticket IDs are case-sensitive and may be reused in different labs.
'''

n = int(input())
tickets = {}

for i in range(n):
    lab, ticket, status = input().split()
    lab = lab.upper()
    tickets[(lab, ticket)] = status


counts = {}

for (lab, ticket), status in tickets.items():
    if status == "OPEN":
        counts[lab] = counts.get(lab, 0) + 1


print('\nOUTPUT\n')
if not counts:
    print("NO OPEN TICKETS")
else:
    for lab, count in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(lab, count)
