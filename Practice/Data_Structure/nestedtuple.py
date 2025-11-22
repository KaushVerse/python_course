# 🚀 Nested Tuples Example
# A tuple that contains other tuples (multi-level structure).

# 📌 Creating a nested tuple
system_specs = (
    ("CPU", ("Brand: Intel", "Model: Core i7", "Cores: 8")),
    ("RAM", ("Type: DDR4", "Size: 16GB", "Speed: 3200MHz")),
    ("Storage", ("Type: SSD", "Capacity: 512GB", "Interface: NVMe")),
)

# 📌 Printing nested tuple data
print("🔧 System Specifications:\n")
for component, details in system_specs:
    print(f"{component}:")
    for item in details:
        print(f"   • {item}")
    print()

# 📌 Accessing individual nested elements
print("🎯 Accessing Specific Values:")
print("CPU Model:", system_specs[0][1][1])      # "Model: Core i7"
print("RAM Size:", system_specs[1][1][1])       # "Size: 16GB"
print("Storage Type:", system_specs[2][1][0])   # "Type: SSD"
