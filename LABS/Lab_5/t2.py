from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass

class Triangle(Shape):

    def Area(self,b,h):
        return  (b*h)/2


class Rectangle(Shape):

    def Area(self, b, h):
        return (b * h)


class Square(Shape):

    def Area(self, b):
        return (b * b)


T = Triangle()
R = Rectangle()
S = Square()

print(f"Area Of Triangle {T.Area(4,6)}")
print(f"Area Of Square {S.Area(4)}")
print(f"Area Of Rectangle {R.Area(4,8)}")

