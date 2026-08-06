# static methods


class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    @staticmethod 
    # static method are decorator of python this will use for static method
    def car_description():
        return "car was good for traveling... 🚙"



print(Car.car_description())