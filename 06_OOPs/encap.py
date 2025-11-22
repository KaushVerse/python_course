class BankAccount:
    """Encapsulation: hide internal state, expose via methods."""
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.__owner = owner  # private attribute
        self.__balance = balance  # private attribute
    
    # Getter methods
    def get_owner(self) -> str:
        return self.__owner
    
    def get_balance(self) -> float:
        return self.__balance
    
    # Setter with validation
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Invalid withdrawal amount")
    
    def __repr__(self) -> str:
        return f"BankAccount(owner={self.__owner!r}, balance=${self.__balance:.2f})"


class Student:
    """Using @property for cleaner getter/setter access."""
    
    def __init__(self, name: str, gpa: float = 0.0):
        self.__name = name
        self.__gpa = gpa
    
    @property
    def name(self) -> str:
        """Getter for name."""
        return self.__name
    
    @property
    def gpa(self) -> float:
        """Getter for GPA."""
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value: float) -> None:
        """Setter with validation."""
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            print("GPA must be between 0.0 and 4.0")
    
    def __repr__(self) -> str:
        return f"Student(name={self.__name!r}, gpa={self.__gpa})"


if __name__ == "__main__":
    # BankAccount example
    account = BankAccount("Alice", 1000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # Invalid
    print(account)
    
    # Student example with @property
    student = Student("Bob", 3.5)
    print(f"\n{student}")
    student.gpa = 3.8  # Valid
    print(student)
    student.gpa = 5.0  # Invalid