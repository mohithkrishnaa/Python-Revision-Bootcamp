#inheritance
#defining base class 
class Car:
    def __init__(self, brand, color, mileage=0):
        self.brand = brand       # Public attribute
        self.color = color       # Public attribute
        self.mileage = mileage   # Public attribute

    def drive(self, distance):
        if distance > 0:
            self.mileage += distance
            return f"Drove {distance} miles. Total mileage is now {self.mileage} miles."
        return "Distance must be positive."

    def get_info(self):
        return f"Brand: {self.brand}, Color: {self.color}, Mileage: {self.mileage} miles"

#defining subclass
class ElectricCar(Car):
    def __init__(self, brand, color, mileage=0, battery_capacity=100):
        super().__init__(brand, color, mileage)  # Call the constructor of the base class
        self.battery_capacity = battery_capacity  # Specific attribute for electric cars

    def charge(self):
        return "The car is charging."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Battery Capacity: {self.battery_capacity}%"

class GasCar(Car):
    def __init__(self, brand, color, mileage=0, fuel_capacity=50):
        super().__init__(brand, color, mileage)  # Call the constructor of the base class
        self.fuel_capacity = fuel_capacity  # Specific attribute for gas cars

    def refuel(self):
        return "The car is refueling."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Fuel Capacity: {self.fuel_capacity} liters"

#instantiate subclass
# Creating instances of ElectricCar and GasCar
tesla = ElectricCar("Tesla", "Red", 5000, 85)
mustang = GasCar("Ford", "Blue", 30000, 60)

# Using methods from the base class and subclasses
print(tesla.get_info())  # Output: Brand: Tesla, Color: Red, Mileage: 5000 miles, Battery Capacity: 85%
print(tesla.charge())    # Output: The car is charging.
print(tesla.drive(150))  # Output: Drove 150 miles. Total mileage is now 5150 miles.

print(mustang.get_info())  # Output: Brand: Ford, Color: Blue, Mileage: 30000 miles, Fuel Capacity: 60 liters
print(mustang.refuel())    # Output: The car is refueling.
print(mustang.drive(200))  # Output: Drove 200 miles. Total mileage is now 30200 miles.
