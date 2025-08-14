# What is a variable?
# Variable ek container hai jisme hum data store karte hain.
# Python mein variable ko define karne ke liye kisi bhi specific type ka declaration nahi karna padta.
# Bas variable ka naam likhna hota hai aur uske baad value assign karni hoti hai.

# Example:
name = "Alice"  # yahan 'name' ek variable hai jisme string value "Alice" store ki gayi hai.
age = 30  # yahan 'age' ek variable hai jisme integer value 30 store ki gayi hai.

# Variable name, Value Alice, Data type string
# Variable age, Value 30, Data type integer 

# Rule:
# Python is dynamically typed language, isliye variable ki type ko explicitly define nahi karna padta.

# Rules for naming variables:
# 1. Variable name sirf letters (a-z, A-Z), digits (0-9) but not a start, aur underscore (_) se shuru ho sakta hai.
# 2. Variable name mein space nahi hona chahiye.
# 3. Variable name case-sensitive hota hai, yani 'name' aur 'Name' alag variables hain.
# 4. Reserved keywords (jaise 'if', 'else', 'while', etc.) ko variable name ke roop mein use nahi kar sakte.

# Varibales Types: (Data Types)
# 1. Integer: Pura sankhya (e.g., 10, -5)
# 2. Float: Decimal sankhya (e.g., 3.14, -0.001)
# 3. String: Textual data (e.g., "Hello", 'World')
# 4. Boolean: True ya False value
# 5. List: Ordered collection of items (e.g., [1, 2, 3], ["apple", "banana"])
# 6. Tuple: Immutable ordered collection (e.g., (1, 2, 3), ("apple", "banana"))
# 7. Dictionary: Key-value pairs (e.g., {"name": "Alice", "age": 30})
# 8. Set: Unordered collection of unique items (e.g., {1, 2, 3}, {"apple", "banana"})
# Range: Range of numbers (e.g., range(1, 10))

# Maping Types:
# 1. List: Ordered collection of items, can contain mixed data types.
# 2. Tuple: Similar to list but immutable, meaning its items cannot be changed after creation.
# 3. Dictionary: Collection of key-value pairs, where each key is unique.
# 4. Set: Unordered collection of unique items, useful for membership testing and eliminating duplicates.
# 5. Range: Represents a sequence of numbers, often used in loops.

# How to check variable type:
print(type(name)) # Output: <class 'str'>, yeh batata hai ki 'name' variable ka type string hai.

# Maping Types Example:
my_list = [1, 2, 3, "apple", "banana"]  # List with mixed data types

print(my_list)  # Output: [1, 2, 3, 'apple', 'banana']

# Set Example:
my_set = {1, 2, 3, "apple", "banana"}  # Set with unique items
fs = frozenset(my_set)  # Immutable version of set
print(fs)  # Output: frozenset({1, 2, 3, 'apple', 'banana'})


# Multiple variable assignment:
x, y, z = 10, 20, 30  # yahan x, y aur z ko ek hi line mein values assign kiye gaye hain.
print(x, y, z)  # Output: 10 20 30

# Memory Management:
# Python mein memory management automatic hota hai, yani jab variable ka scope khatam ho jata hai,
# to Python garbage collector us memory ko free kar deta hai.
# Isliye hume manually memory manage karne ki zarurat nahi padti.
# Lekin agar hume kisi variable ki zarurat nahi hai, to usse del statement se delete kar sakte hain.
del name  # yeh 'name' variable ko delete kar deta hai.
# Agar hum del ke baad 'name' variable ko access karne ki koshish karte hain, to error aayega.
# print(name)  # Uncommenting this line will raise a NameError since 'name' is deleted.

# Memory Management & id():
# Python mein har variable ka ek unique id hota hai, jo uski memory address ko represent karta hai.
print(id(age))  # Output: Unique memory address of 'age' variable

# Variable Scope:
# Variable scope ka matlab hai ki variable kis jagah tak accessible hai.
# Python mein variable ka scope function ke andar aur bahar alag hota hai.
# Agar variable function ke andar define kiya gaya hai, to uska scope sirf us function tak hi hota hai.
# Agar variable global scope mein define kiya gaya hai, to wo poore program mein accessible hota hai.

# Example of variable scope:
def my_function():
    local_var = "I am local"
    print(local_var)  # yeh local variable function ke andar accessible hai.

my_function()  # Output: I am local
# print(local_var)  # Uncommenting this line will raise a NameError since 'local_var' is not accessible outside the function.

# Constants in Python:
# Python mein constants ko define karne ka koi specific syntax nahi hai,
# lekin convention ke roop mein hum constant variable names ko uppercase mein likhte hain.
PI = 3.14  # yeh ek constant hai, iski value change nahi karni chahiye.
print(PI)  # Output: 3.14

# Summary Table:
# | Concept                     | Description                                   | Example              |
# |----------------------------|-----------------------------------------------|----------------------|
# | Variable Creation         | Assign value with                             | name = "Alice"       |
# | Type Inference           | Python detects type automatically             | type(x)              |
# | Variable Naming         | Rules for naming variables                    | my_var = 10          |
# | Dynamic Typing         | Type can change later                         | x = 5 => x = 'hi'    |
# | Multiple Assignment   | Assign multiple variables in one line         | x, y, z = 1, 2, 3    |
# | Memory Reference     | Reuses memory for immutables                  |id(a) == id(b)        |
# | Variable Scope      | Locol, Global, NonLocal                       |  global x            |
# | Constants          | Convention for constants                      | PI = 3.14            |

