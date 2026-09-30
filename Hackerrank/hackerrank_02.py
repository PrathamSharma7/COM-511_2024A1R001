'''
A student records monthly expenses under different categories. Write a program that combines the expenses for each category and reports the total amount spent. Category names are case-insensitive. For example, Food, FOOD, and food represent the same category. Display: 1. The total monthly expense. 2. Each category and its total, ordered from highest to lowest expenditure. 3. The category with the highest expenditure. If two categories have the same expenditure, display them in alphabetical order. If multiple categories tie for the highest expenditure, the alphabetically first category is the highest-spending category reported. Input Format

The first line contains an integer n, the number of expense entries.
Each of the next n lines contains a category name and an amount, separated by a space.
Category names contain no spaces.
Input Format

6 Food 250.50 Travel 120 FOOD 99.50 Books 300 travel 80 food 50

Constraints

1 ≤ n ≤ 1000 1 ≤ category name length ≤ 30 Category names contain letters only. 0 < amount ≤ 1000000 Amounts have up to two digits after the decimal point.

Output Format

Print the total monthly expense to two decimal places.
Print the category totals in descending order of expenditure. If two categories have the same total, print them in alphabetical order. Print each amount to two decimal places.
Finally, print the alphabetically first category with the highest expenditure and its total.
Sample Input 0

6
Food 250.50
Travel 120
FOOD 99.50
Books 300
travel 80
food 50
Sample Output 0

Total Monthly Expense: 900.00
Expenses by Category:
food : 400.00
books : 300.00
travel : 200.00
Highest Expense Category: food
Highest Expense Amount: 400.00
'''