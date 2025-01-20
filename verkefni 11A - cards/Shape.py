

# shape.py
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area calculation.")

    def perimeter(self) -> float:
        raise NotImplementedError("Subclasses must implement perimeter calculation.")

    def __str__(self) -> str:
        return f"{type(self).__name__} with area of {self.area():.2f} and perimeter of {self.perimeter():.2f}."
