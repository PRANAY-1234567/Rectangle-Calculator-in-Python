class Rectangle:
    def __init__(self):
        self.length = 0.0
        self.breadth = 0.0

    def input(self):
        self.length = float(input("Enter the Length : "))
        self.breadth = float(input("Enter the Breadth : 65"))

    def area(self):
        a = self.length * self.breadth
        print("Area of rectangle :", a)

    def perimeter(self):
        p = 2* (self.length + self.breadth)
        print("Perimeter of rectangle :", p)

react = Rectangle()
react.input()
react.area()
react.perimeter()

