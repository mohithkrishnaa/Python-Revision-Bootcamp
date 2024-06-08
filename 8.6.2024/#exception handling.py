#exception handling
# Exception handling in Python is a way to manage errors and other exceptional events in a program.
#  It helps to prevent crashes and allows you to respond to errors gracefully. 
# The main constructs for exception handling in Python are try, except, else, and finally.

#def class car
class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - ${self.price}"

    def update_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

#def class car company
class CarCompany:
    def __init__(self):
        self.cars = {}

    def add_car(self, car_id, car):
        if car_id in self.cars:
            raise ValueError(f"Car ID {car_id} already exists.")
        self.cars[car_id] = car

    def get_car(self, car_id):
        if car_id not in self.cars:
            raise KeyError(f"Car ID {car_id} not found.")
        return self.cars[car_id]

    def update_car_price(self, car_id, new_price):
        try:
            car = self.get_car(car_id)
            car.update_price(new_price)
        except KeyError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")

    def display_cars(self):
        for car_id, car in self.cars.items():
            print(f"ID: {car_id} - {car}")

# Example usage
company = CarCompany()

try:
    # Adding cars
    company.add_car(1, Car("Toyota", "Camry", 2020, 24000))
    company.add_car(2, Car("Tesla", "Model S", 2021, 79999))

    # Displaying cars
    company.display_cars()

    # Updating car price
    company.update_car_price(2, 74999)

    # Displaying cars after price update
    company.display_cars()

    # Attempting to update with a negative price
    company.update_car_price(2, -5000)

    # Attempting to add a car with an existing ID
    company.add_car(1, Car("Honda", "Civic", 2019, 20000))

except ValueError as e:
    print(f"ValueError: {e}")
except KeyError as e:
    print(f"KeyError: {e}")

finally:
    print("Car company operations completed.")
