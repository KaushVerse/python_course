class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object of the Car class
my_car = Car("Honda", "Civic", 2022)
car_info = my_car.display_info()  # Method Invocation
print(car_info)  # Output: 2022 Honda Civic