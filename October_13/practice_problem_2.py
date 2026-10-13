'''
Instance methods: Rectange Area and perimeter
'''

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def perimeter(self):
        return 2*(self.length + self.width)
    def area(self):
        return self.length * self.width

rect1 = Rectangle(20,10)
print(f'''Perimeter = {rect1.perimeter()}\nArea: {rect1.area()}''')