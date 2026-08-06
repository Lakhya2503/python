# is Instance

class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

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

isCar = isinstance(my_atto, Car) 
isCarInstance = isinstance(my_x1, Car) 

print(f"isCar : {isCar}") 
print(f"isCarInstance : {isCarInstance}")
# both are true beacuse it will the main class is Car

