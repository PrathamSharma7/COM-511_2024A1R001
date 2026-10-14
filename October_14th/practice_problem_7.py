'''
Create an Employee class that stores an employee's name, basic salary, house rent allowance (HRA) percentage,
travel allowance and deductions. Add instance methods to calculate the gross salary and net salary.
Gross salary is the basic salary plus HRA and travel allowance. Net salary is the gross salary minus deductions.
Display the employee's name, gross salary and net salary.
'''

class Employee:
    def __init__(self, name, basic_salary, house_rent_allowance_percentage, travel_allowance, deductions):
        self.name = name
        self.basic_salary = basic_salary
        self.house_rent_allowance_percentage = house_rent_allowance_percentage
        self.travel_allowance = travel_allowance
        self.deductions = deductions

    def calculate_gross_salary(self):
        self.gross_salary = self.basic_salary + (self.house_rent_allowance_percentage*self.basic_salary/100) + self.travel_allowance
        return self.gross_salary

    def calculate_net_salary(self):
        self.net_salary = self.gross_salary - self.deductions

    def display_salary(self):
        print(f"Name: {self.name}\nGross Salary: {self.gross_salary}\nNet Salary: {self.net_salary}")

name = input("Enter Employee Name: ")
bs = float(input("Enter Basic Salary: "))
hra = float(input("Enter House Rent Allowance Percentage: "))
ta = float(input("Enter Travel Allowance: "))
deductions = float(input("Enter Deductions: "))

emp1 = Employee(name, bs, hra, ta, deductions)
emp1.calculate_gross_salary()
emp1.calculate_net_salary()
emp1.display_salary()