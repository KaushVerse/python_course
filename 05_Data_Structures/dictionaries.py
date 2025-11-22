# 📖 Dictionary ek unordered, mutable, aur key–value pair data structure hoti hai. Each key uniquely identifies a value 🔑➡️📦

student = {
    "name": "Chhotu",
    "age": 22,
    "role": "Engineer"
}

# 🎯 Yahaan "name", "age", "role" → keys hain
# aur "Chhotu", 22, "Engineer" → values hain.

# ⚙️ Key Features

# | 🔹 Feature                   | 📖 Description                     |
# | --------------------------- | ---------------------------------- |
# | 🧱 **Key-Value Pairs**     | Store data as `{key: value}`       |
# | 📦 **Mutable**            | Add / remove / modify items        |
# | 🗝️ **Unique Keys**       | No duplicate keys allowed          |
# | ⚡ **Fast Lookup**      | Access via keys (hash table based) |
# | 🔄 **Dynamic**         | Can grow or shrink easily          |
# | 🌈 **Mixed Data**     | Keys and values can be of any type |


# 🖋️ Creating a Dictionary

# | 🧩 Method            | 💡 Example                     | 🎯 Output          |
# | -------------------- | ------------------------------ | ------------------ |
# | Curly braces `{}`    | `{"a": 1, "b": 2}`             | Normal dictionary  |
# | `dict()` constructor | `dict(a=1, b=2)`               | Same output        |
# | From list of tuples  | `dict([("x", 10), ("y", 20)])` | `{'x':10, 'y':20}` |
# | Empty dictionary     | `{}`                           | Empty              |


student = {"name": "Chhotu", "age": 22, "role": "Engineer"}

print(student["name"])    # Chhotu
print(student.get("age")) # 22

# ⚠️ Difference:

# student["key"] → ❌ Error if key doesn’t exist
# student.get("key") → ✅ Returns None if not found

# 🧱 Adding / Updating Elements

student["city"] = "Delhi"        # Add new
student["age"] = 23              # Update existing


# 🧠 Nested Dictionaries

students = {
  "name": "Student Data",
  "s1": {"name": "Chhotu", "age": 22},
  "s2": {"name": "Raj", "age": 21}
}
print(students["s1"]["name"])  # Chhotu


# ⚡ Dictionary Unpacking

info = {"name": "Chhotu", "role": "Engineer"}
print("Hello", **info) # Hello Chhotu Engineer


# 🧩 Key Conversion via Type Casting

# Agar input me key number form me string aa rahi hai,
# toh manually cast kar sakte ho 👇

data = {"1": "String Key"}
key = int("1")
print(data.get(key))  # None ❌
print(data.get(str(key)))  # ✅ Works


# 🧩 Dynamic Keys (User Input / Loops)

d = {}
for i in range(3):
    d[f"user{i}"] = i
print(d)


# 🧩 Using Expressions as Keys

data = {1+2: "Sum", len("Hi"): "Length"}
print(data)


# 🧩 Using Variables as Keys

key1 = "name"
key2 = 100
data = {key1: "Chhotu", key2: "Engineer"}
print(data)


# 🧩 Tuple Keys Deep Dive

valid = {(1, 2, 3): "Numbers"}
invalid = {([1, 2], 3): "List Inside"}  # ❌ Error


# 🧩 Same Hash Keys (Collisions Concept)

data = {1: "Int Key", True: "Bool Key"}
print(data)
# True ka hash value 1 ke barabar hota hai (hash(True) == hash(1))
# Toh dono same key treat hote hain — last value overwrite kar deti hai.