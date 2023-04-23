import App.Utilities.units as Units
import math

# A class that is used to managed general shapes for wepons and spells (potentially)
# For instance this is called to manage the dragonborn ability


class Shape:
    def __init__(self) -> None:
        pass


# A class for 2D shapes
class Shape2D(Shape):
    def __init__(self) -> None:
        super().__init__()

# A class for 3D shapes


class Shape3D(Shape):
    def __init__(self) -> None:
        super().__init__()


# Classes that is used to manage specific shapes
# 2D Shapes
class Rectangle(Shape2D):
    def __init__(self, length: int, width: int) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def area(self) -> float:
        # Returns the area of the rectangle
        return self.length * self.width

    def perimeter(self) -> float:
        # Returns the perimeter of the rectangle
        return 2*self.length + 2*self.width

# 3D Shapes


class Cone(Shape3D):
    def __init__(self, height: int, angle: int = 20) -> None:
        super().__init__()
        self.height = height
        self.angle = angle
        self.radius = round(self.height/math.tan(math.radians(self.angle)), 3)
        self.length = round(math.sqrt(self.height**2 + self.radius**2), 3)

    def volume(self) -> float:
        return round((math.pi * (self.radius**2) * self.height) / 3, 3)

    def surface(self) -> float:
        return math.pi * self.radius * (self.radius + self.length)
