#defining abstraction
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def drive(self):
        print("Driving the car...")

#implementing
class ElectricCar(Car):
    def start_engine(self):
        print("Starting the electric engine silently...")

    def stop_engine(self):
        print("Stopping the electric engine silently...")

class GasCar(Car):
    def start_engine(self):
        print("Starting the gas engine with a roar...")

    def stop_engine(self):
        print("Stopping the gas engine with a roar...")

#demonstration
# Create an instance of ElectricCar
tesla = ElectricCar()
tesla.start_engine()  # Output: Starting the electric engine silently...
tesla.drive()         # Output: Driving the car...
tesla.stop_engine()   # Output: Stopping the electric engine silently...

# Create an instance of GasCar
mustang = GasCar()
mustang.start_engine()  # Output: Starting the gas engine with a roar...
mustang.drive()         # Output: Driving the car...
mustang.stop_engine()   # Output: Stopping the gas engine with a roar...