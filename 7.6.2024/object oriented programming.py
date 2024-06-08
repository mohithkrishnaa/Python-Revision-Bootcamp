#object oriented programming
#special methods

#__init__ method
class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price

#__str__ method
    def __str__(self):
        return f"Car with color {self.color} and price {self.price}"
