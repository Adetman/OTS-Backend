#Create a Car Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_description(self):
        return f"{self.brand} {self.model}"

#Create an instance of the Car class
my_car = Car("Toyota", "Corolla")

#Print the description of the car
print(my_car.get_description())

