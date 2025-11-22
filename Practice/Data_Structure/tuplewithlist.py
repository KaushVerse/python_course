# 🚀 Tuple of Lists Example
# A tuple contains multiple lists. Each list stores related items.

# 📌 Tuple containing lists
system_info = (
    ["Intel Core i7", "AMD Ryzen 5"],        # CPU list
    ["8GB DDR4", "16GB DDR4", "32GB DDR4"],  # RAM list
    ["256GB SSD", "512GB SSD", "1TB SSD"],   # Storage list
)

# 📌 Accessing lists inside tuple
print("🔧 System Configuration Options:\n")
print("Available CPUs:", system_info[0])
print("Available RAMs:", system_info[1])
print("Available Storage Options:", system_info[2])

# 📌 Accessing individual items
print("\n🎯 Accessing Specific Items:")
print("First CPU:", system_info[0][0])
print("Second RAM Option:", system_info[1][1])
print("Third Storage Option:", system_info[2][2])


# 🚀 Tuple of Lists with Product Information
products = (
    ["Laptop", "Headphones", "Keyboard"],        # product names
    [45000, 2000, 1500],                          # prices
    ["Electronics", "Accessories", "Accessories"] # category
)

print("🛒 Product List:")
for i in range(len(products[0])):
    print(f"{products[0][i]} - ₹{products[1][i]} ({products[2][i]})")
