import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if the triangle is valid
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
    exit(0)

# Sort the sides
sides = sorted([a, b, c])

# Check if right-angled
if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Right-angled triangle")
else:
    print("Not a right-angled triangle")

# Calculate area using Heron's formula
s = (a + b + c) / 2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f"Area = {area:.2f}")