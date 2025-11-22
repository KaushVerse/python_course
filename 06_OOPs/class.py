class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand # Instance variable
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        return f"The engine of the {self.brand} {self.model} is starting."
    
# Object Creation
my_car = Car("Toyota", "Camry", 2020, "Blue")
start_car = my_car.start_engine()  # Method Invocation

print(start_car)  # Output: The engine of the Toyota Camry is starting.