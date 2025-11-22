class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"


# Single inheritance + polymorphism
class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# Multilevel inheritance
class Puppy(Dog):
    def speak(self):
        # reuse parent's behavior and extend it
        return f"{super().speak()} (whines)"


# Mixins and multiple inheritance
class FlyMixin:
    def fly(self):
        return f"{self.name} is flying"


class SwimMixin:
    def swim(self):
        return f"{self.name} is swimming"


class Duck(Animal, FlyMixin, SwimMixin):
    def speak(self):
        return "Quack"


if __name__ == "__main__":
    animals = [
        Dog("Rex"),
        Cat("Misty"),
        Puppy("Buddy"),
        Duck("Daffy"),
    ]

    for a in animals:
        print(a, "-> speak:", a.speak())
        # show mixin capabilities if present
        if hasattr(a, "fly"):
            print("   fly:", a.fly())
        if hasattr(a, "swim"):
            print("   swim:", a.swim())

    # Demonstrate MRO for multiple inheritance
    print("\nDuck MRO:", [cls.__name__ for cls in Duck.__mro__])