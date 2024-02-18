
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an instance of Car
my_car = Car("Tesla", "Model S", 2020)
print(my_car.get_description())
