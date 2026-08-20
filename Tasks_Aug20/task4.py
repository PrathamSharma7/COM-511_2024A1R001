#Write a Python program to ask the user for radius and calculate area and circumference of a circle

radius = float(input("Enter radius: "))
pi = 3.141459
area = pi*radius*radius
circumference = 2*pi*radius
print("Area of circle:", area)
print("Circumference of circle:", circumference)