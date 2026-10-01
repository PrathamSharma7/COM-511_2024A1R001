'''
Instance methods: Rectangle area and perimeter
Problem: Create a class Rectangle with length and breadth. Use instance methods to calculate
its area and perimeter.
'''
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

r1 = Rectangle(4,5)
print(r1.area(), r1.perimeter())