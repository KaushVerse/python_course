# 🚀 List with Tuple Example
# This script shows how to store structured data using a list of tuples.

# 📌 Creating a list of tuples (Component Name, Component Detail)
components = [
    ("CPU", "Intel Core i7"),
    ("RAM", "16GB DDR4"),
    ("Storage", "512GB SSD"),
    ("GPU", "NVIDIA GTX 1660"),
]

# 📌 Printing all components
print("🔧 System Components:\n")
for name, detail in components:
    print(f"{name}: {detail}")

# 📌 Accessing individual tuple elements
print("\n🎯 Accessing Specific Items:")
first_name, first_detail = components[0]
second_name, second_detail = components[1]

print(f"First Component: {first_name} - {first_detail}")
print(f"Second Component: {second_name} - {second_detail}")


# 🚀 List of Tuples with Dictionaries Inside
# Each tuple = (Component Name, Component Details as a Dictionary)

components = [
    ("CPU", {"brand": "Intel", "model": "Core i7", "cores": 8, "clock": "3.8GHz"}),
    ("RAM", {"type": "DDR4", "size": "16GB", "speed": "3200MHz"}),
    ("Storage", {"type": "SSD", "capacity": "512GB", "interface": "NVMe"}),
    ("GPU", {"brand": "NVIDIA", "model": "GTX 1660", "vram": "6GB"}),
]

# 📌 Printing all components nicely
print("🔧 System Components:\n")
for name, details in components:
    print(f"{name}:")
    for key, value in details.items():
        print(f"   • {key.capitalize()}: {value}")
    print()

# 📌 Accessing a specific component's details
print("🎯 Accessing Specific Items:")
gpu_details = components[3][1]   # second item of tuple = dictionary
print("GPU Model:", gpu_details["model"])


# 🚀 List of Tuples with User Information
users = [
    (1, {"name": "Rahul", "email": "rahul@example.com", "role": "admin"}),
    (2, {"name": "Aisha", "email": "aisha@example.com", "role": "editor"}),
    (3, {"name": "Kabir", "email": "kabir@example.com", "role": "viewer"}),
]

print("🧑‍💻 Users:\n")
for user_id, info in users:
    print(f"ID: {user_id}")
    for key, value in info.items():
        print(f"   • {key.capitalize()}: {value}")
    print()


# 🚀 List of Tuples with Order Information
orders = [
    (
        101,
        {
            "user": "Rahul",
            "items": [("Laptop", 1), ("Keyboard", 1)],
            "total": 46500,
            "status": "Shipped",
        },
    ),
    (
        102,
        {
            "user": "Aisha",
            "items": [("Headphones", 2)],
            "total": 4000,
            "status": "Pending",
        },
    ),
]

print("📦 Orders:\n")
for order_id, info in orders:
    print(f"Order ID: {order_id}")
    print(f"User: {info['user']}")
    print("Items:")
    for item, qty in info["items"]:
        print(f"   • {item} x{qty}")
    print(f"Total Amount: ₹{info['total']}")
    print(f"Status: {info['status']}\n")
