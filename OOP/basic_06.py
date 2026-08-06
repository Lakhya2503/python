# decorators

class Car:
    def __init__(self, brand, model):
        self.__model = model
        self.__brand = brand

    @staticmethod 
    def car_description():
        return "car was good for traveling... 🚙"

    
    @property
    # when you add the property decorator then use like object ex. car.model 
    # it will convert like object
    def model(self):
        return self.__model

my_car = Car("Tata", "Baleno")
# my_car.model = "safari"
# print(my_car.model)