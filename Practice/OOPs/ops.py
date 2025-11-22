class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
s1 = Student("Alice", 20, "A")
print(s1.get_details())  # Output: Name: Alice, Age: 20, Grade: A


class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
c1 = Car("Toyota", "Camry", 2020)
print(c1.get_info())  # Output: 2020 Toyota Camry