# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# ZDE DOPLŇTE VLASTNÍ KÓD
class Rectangle(Shape):
    def __init__(self,width,height):
        self._width = width
        self._height = height
    def area(self):
        return self._height * self._width
    pass

class Circle(Shape):
    def __init__(self,radius):
        self._radius = radius
    def area(self):
        return math.pi * (self._radius**2)
    pass


from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass