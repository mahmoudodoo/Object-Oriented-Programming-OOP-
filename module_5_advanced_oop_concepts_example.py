
class BaseClass:
    def method(self):
        return 'BaseClass method called'

class ChildClass1(BaseClass):
    def method(self):
        return 'ChildClass1 method called'

class ChildClass2(BaseClass):
    def method(self):
        return 'ChildClass2 method called'

# Multiple Inheritance
class MultipleInheritance(ChildClass1, ChildClass2):
    pass

# Operator Overloading
class Length:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return self.value

# Composition
class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

# Demonstrating Usage
multiple_inheritance_instance = MultipleInheritance()
print(multiple_inheritance_instance.method())

length_instance = Length(5)
print(len(length_instance))

car_instance = Car()
car_instance.start()
