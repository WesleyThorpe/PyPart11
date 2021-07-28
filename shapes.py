from typing import TypeVar

x = TypeVar('x', int,float)

class Rectangle: 
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width) 

class Square(Rectangle):
    def __init__(self, x):
        super().__init__(x,x)


newSquare = Square(8)    

print(newSquare.area())
print(newSquare.perimeter())