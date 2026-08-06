# multiple inheritance

class Battery:
    def battery_info(self):
        return f" This is Battery info "
    

class Engine:
    def engine_info(self):
        return f" This is Engine info "

class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def fule_type(self):
        return f" Petrol or Diesel "


class ElectricalCar(Battery, Engine, Car):
    pass

my_new_tato = ElectricalCar("tato", "Model Z")
print(my_new_tato.engine_info())
print(my_new_tato.battery_info())