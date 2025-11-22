from abc import ABC, abstractmethod


# Abstract base class
class Vehicle(ABC):
    """Abstract class defining interface for all vehicles."""
    
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start(self) -> str:
        """All vehicles must implement start."""
        pass
    
    @abstractmethod
    def stop(self) -> str:
        """All vehicles must implement stop."""
        pass
    
    @abstractmethod
    def get_speed(self) -> float:
        """All vehicles must implement get_speed."""
        pass


class Car(Vehicle):
    """Concrete implementation of Vehicle."""
    
    def __init__(self, brand: str, model: str, fuel_type: str):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.speed = 0.0
    
    def start(self) -> str:
        return f"{self.brand} {self.model} started with {self.fuel_type}"
    
    def stop(self) -> str:
        self.speed = 0.0
        return f"{self.brand} {self.model} stopped"
    
    def get_speed(self) -> float:
        self.speed = 100.0
        return self.speed


class Bike(Vehicle):
    """Another concrete implementation of Vehicle."""
    
    def __init__(self, brand: str, model: str, bike_type: str):
        super().__init__(brand, model)
        self.bike_type = bike_type
        self.speed = 0.0
    
    def start(self) -> str:
        return f"{self.brand} {self.model} ({self.bike_type}) started"
    
    def stop(self) -> str:
        self.speed = 0.0
        return f"{self.brand} {self.model} stopped"
    
    def get_speed(self) -> float:
        self.speed = 80.0
        return self.speed


if __name__ == "__main__":
    # Cannot instantiate abstract class directly
    # vehicle = Vehicle("Generic", "Model")  # Error!
    
    vehicles = [
        Car("Toyota", "Camry", "Petrol"),
        Bike("Harley-Davidson", "Street 750", "Cruiser"),
    ]
    
    for v in vehicles:
        print(f"\n{v.brand} {v.model}")
        print(f"  Start: {v.start()}")
        print(f"  Speed: {v.get_speed()} km/h")
        print(f"  Stop: {v.stop()}")