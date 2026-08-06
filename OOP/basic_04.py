# polymorphism

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.model = model
        self.brand = brand
        Car.total_car += 1 
        # can't add the self beacuse when i Car.total_car then he will access the 
        # main total_car when Car.total_car then count the total_car created

    def fule_type(self):
        return f" Petrol or Diesel "


class ElectricalCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fule_type(self):
        return f" Electrical Charge "

my_x1 = Car("BMW","x1")
print(f"my_x1 : {my_x1.fule_type()}")

my_atto = ElectricalCar("BYD","Atto 3")
print(f"my_atto : {my_atto.fule_type()}")

print(Car.total_car) 