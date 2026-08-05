# Basic class and object

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

my_car = Car("BMW", "m5")
print(f""" my from italy was { my_car.brand } on { my_car.model } edition """)