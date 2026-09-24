'''
Write a Python program to store two points as tuples and calculate the distance between them
'''
import math
x1 = float(input("Enter x-coordinate of point 1:"))
y1 = float(input("Enter y-coordinate of point 1:"))
x2 = float(input("Enter x-coordinate of point 2:"))
y2 = float(input("Enter y-coordinate of point 2:"))

point1 = (x1, y1)
point2 = (x2, y2)

distance = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

print(f"distance between {point1} and {point2} = {distance}")