
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self._name = name  # protected attribute

    @abstractmethod
    def display_info(self):
        pass

class Car(Vehicle):
    def display_info(self):
        return f"Car name: {self._name}"

# Using encapsulation
car = Car("Tesla Model S")
print(car.display_info())

# Trying to access the protected attribute directly (not recommended)
# print(car._name)
