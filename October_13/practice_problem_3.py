'''
Create a product class with product name, price and quantity. 
Add an instance method to calculate total cost.
Take these values from user and display product name and total cost.
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_cost(self):
        self.total_cost = self.price * self.quantity
        return self.total_cost

    def display_details(self):
        print(f"Name: {self.name}\nTotal Cost: {self.total_cost}")

pname = input("Enter product name: ")
pprice = float(input("Enter product price: "))
pquant = int(input("Enter product quantity: "))
product_1 = Product(pname, pprice, pquant)
print(product_1.calculate_total_cost())
print()
product_1.display_details()