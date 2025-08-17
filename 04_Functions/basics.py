# Function Syntax

# def function_name(parameters):
#     """Docstring (optional): Function ka explanation"""
#     # Function body
#     return result  # optional


# Basic Example
def greet():
    print("Hello, Cutie Bro 🥰")


greet() # Function call


# Function with Parameters
def greet(name):
    print(f"Hello {name} 🥰")

greet("Kaushik")


# Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


# Default Parameters
def gret(name="Bro"):
    print(f"Hello {name}")


gret()
gret('Kaushik')

# Keyword Arguments
def intro(name, age):
    print(f"My name is {name} and I am {age} years old")


intro(age=21, name="Kaushik")


# Variable-length Arguments
def demo(*args, **kwargs):
    print("Args", args)
    print("Kwargs", kwargs)


demo(1, 2, 3, name="Kaushik", age=21)


# Docstring (Function Documentation)
def square(x):
    """This function returns square of a number."""
    return x * x

print(square.__doc__)
print(square(2))
