#encapsulation
class Car:
    def __init__(self, brand, color, mileage=0):
        self.__brand = brand       # Strongly private attribute
        self.__color = color       # Strongly private attribute
        self.__mileage = mileage   # Strongly private attribute

    # Public method to get the car's brand
    def get_brand(self):
        return self.__brand

    # Public method to set the car's color
    def set_color(self, color):
        self.__color = color

    # Public method to get the car's color
    def get_color(self):
        return self.__color

    # Public method to get the car's mileage
    def get_mileage(self):
        return self.__mileage

    # Public method to drive the car, increasing the mileage
    def drive(self, distance):
        if distance > 0:
            self.__mileage += distance
            return f"Drove {distance} miles. Total mileage is now {self.__mileage} miles."
        return "Distance must be positive."

# Example usage
car1 = Car("Toyota", "Red", 10000)

# Accessing public methods to get car details
print(car1.get_brand())    # Output: Toyota
print(car1.get_color())    # Output: Red
print(car1.get_mileage())  # Output: 10000
