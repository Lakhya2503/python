# inheritance
from basic_01 import Car

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) #use the Car __init__ and use the brand and model
        self.battery_size = battery_size


my_ioniq = ElectricCar("Hyundai","Ioniq 5", "77.4 kWh")
print(my_ioniq.return_a_brand_and_model())