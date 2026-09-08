'''
Write a python program to calculate the final bill amount after applying a discount. The program should the total bill amount as input from the user 
and apply the discount according to the following rules.
After calculating the discount, the program should display the discount amount and the final bill amount payable by the customer.
Bill Amt        Discount
Above 5000       20%
3000 to 5000     10%
Below 3000       No discount
'''
bill_amount = float(input("Enter Bill Amount: "))
if bill_amount < 3000:
    discount = 0
elif 3000 <= bill_amount < 5000:
    discount = 0.1*bill_amount
else:
    discount = 0.2*bill_amount

print(f"Discount: {discount} \nBill Amount: {bill_amount-discount}")

