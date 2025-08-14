# Numeric Types
num_int = 10
print("int:", num_int, "| Type", type(num_int))

num_float = 10.5
print("float:", num_float, "| Type", type(num_float))

num_complex = 3 + 4j
print("complex:", num_complex, "| Type", type(num_complex))

# Text Type
name = "Alice"
print("str:", name, "| Type", type(name))

# Sequence Types
my_list = [1, 2, 3, "apple", "banana"]
print("list:", my_list, "| Type", type(my_list))

# Tuple Types
my_tuple = (1, 2, 3, "apple", "banana")
print("tuple:", my_tuple, "| Type", type(my_tuple))

my_range = range(5)
# print("range:", my_range, "| Type", type(my_range))
print("range:", list(my_range), "| Type", type(my_range))

# Mapping Type
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("dict:", my_dict, "| Type", type(my_dict))

# Set Types
my_set = {1, 2, 3, "apple", "banana"}
print("set:", my_set, "| Type", type(my_set))

# my_frozenset = frozenset(my_set)
my_frozenset = frozenset([1, 2, 3])
print("frozenset:", my_frozenset, "| Type", type(my_frozenset))

# Boolean Type
is_active = True
print("bool:", is_active, "| Type", type(is_active))

# Binary Types
my_bytes = b"Hello"
print("bytes:", my_bytes, "| Type", type(my_bytes))

my_bytearray = bytearray(my_bytes)
# my_bytearray = memoryview(b"Hello")
print("bytearray:", my_bytearray, "| Type", type(my_bytearray))

# None Type
my_none = None
print("NoneType:", my_none, "| Type", type(my_none))


# All Data Types
all_data_types = {
    "int": num_int,
    "float": num_float,
    "complex": num_complex,
    "str": name,
    "list": my_list,
    "tuple": my_tuple,
    "range": list(my_range),
    "dict": my_dict,
    "set": my_set,
    "frozenset": my_frozenset,
    "bool": is_active,
    "bytes": my_bytes,
    "bytearray": my_bytearray,
    "NoneType": my_none
}

# Print all data types
# for data_type, value in all_data_types.items():
#     print(f"{data_type}: {value} | Type: {type(value)}")
