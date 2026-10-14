'''
Create an ElectricityBill class that stores a customer's name and electricity units used.
Create the bill using these rates:
₹3 per unit for the first 100 units
₹5 per unit for the next 100 units
₹7 per unit for units above 200
Add a fixed charge of ₹50.
Display the customer's name, units used, and total bill amount.
If the entered units are negative, display an error message.
'''

class ElectricityBill:
    def __init__(self, name, units):
        self.customer_name = name
        self.units_used = units

    def calculate_bill(self):
        if self.units_used < 0:
            print("Error: Units used cannot be negative.")
            return None

        bill_amount = 50
        if self.units_used <= 100:
            bill_amount += self.units_used * 3
        elif self.units_used <= 200:
            bill_amount += (100 * 3) + ((self.units_used - 100) * 5)
        else:
            bill_amount += (100 * 3) + (100 * 5) + ((self.units_used - 200) * 7)

        return bill_amount

    def display_bill(self):
        total_bill = self.calculate_bill()
        if total_bill is not None:
            print(f"Customer Name: {self.customer_name}")
            print(f"Units Used: {self.units_used}")
            print(f"Total Bill Amount: ₹{total_bill}")

customer_name = input("Enter customer name: ")
units_used = int(input("Enter electricity units used: "))
bill = ElectricityBill(customer_name, units_used)
bill.display_bill()