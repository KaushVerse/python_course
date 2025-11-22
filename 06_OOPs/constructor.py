class Person:
    def __init__(self, name: str = "Unknown", age: int = 0):
        """Default / parameterized constructor."""
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

    @classmethod
    def from_dict(cls, data: dict):
        """Alternative constructor from a dict."""
        return cls(data.get("name", "Unknown"), data.get("age", 0))


class Employee(Person):
    def __init__(self, name: str, age: int, emp_id: str, position: str = "Staff"):
        """Subclass constructor calls super().__init__ to reuse initialization."""
        super().__init__(name, age)
        self.emp_id = emp_id
        self.position = position

    def __repr__(self):
        return f"Employee(name={self.name!r}, age={self.age}, emp_id={self.emp_id!r}, position={self.position!r})"


if __name__ == "__main__":
    p1 = Person()  # default
    p2 = Person("Alice", 30)  # parameterized
    p3 = Person.from_dict({"name": "Bob", "age": 25})  # alternative constructor
    e1 = Employee("Carol", 28, "E123", "Engineer")  # subclass

    print(p1)
    print(p2)
    print(p3)
    print(e1)

    p2.birthday()
    print("After birthday:", p2)