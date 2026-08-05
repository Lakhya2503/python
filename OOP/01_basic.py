# Basic class and object

class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def return_a_brand_and_model(self):
        return f" Brand is : {self.brand} , model is : {self.model}"

my_car = Car("BMW", "m5")
print(f""" my from italy was { my_car.brand } on { my_car.model } edition """)
print(my_car.return_a_brand_and_model())