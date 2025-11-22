# 📖 List ek ordered, mutable (changeable) collection hoti hai — jo multiple values ko ek hi variable me store karti hai.

# 🧱 List Features (with icons)

# | ⚙️ Feature           | 📖 Description                          |
# | -------------------- | --------------------------------------- |
# | 📦 **Mutable**       | You can change, add, or remove elements |
# | 🔢 **Indexed**       | Access items by index (0-based)         |
# | 🔁 **Ordered**       | Maintains insertion order               |
# | 🌈 **Heterogeneous** | Can store different data types          |
# | ♻️ **Iterable**      | You can loop through it using `for`     |

# 🖋️ Creating Lists

# | 📋 Method         | 💡 Example          | 🎯 Output |
# | ----------------- | ------------------- | --------- |
# | Square Brackets   | `x = [1,2,3]`       | `[1,2,3]` |
# | `list()` Function | `x = list((1,2,3))` | `[1,2,3]` |
# | Empty List        | `x = []`            | `[]`      |

# 🧩 Accessing Elements (Nested Lists)

data = [1, [2, 3], 4]
print(data[1][0])  # 2

# 🧾 Summary Table (Cheat Sheet with Icons)

# | 📦 Concept             | 🧠 Description                     | 💡 Example       |
# | --------------------- | ---------------------------------- | ---------------- |
# | ✨ Create            | `[1,2,3]`, `list((1,2))`           | Create list      |
#  🎯 Index             | `lst[0]`, `lst[-1]`                | Access items     |
# | ✂️ Slice           | `lst[1:3]`                         | Part of list     |
# | ➕ Add            | `append()`, `insert()`, `extend()` | Add items        |
# | ➖ Remove         | `remove()`, `pop()`, `clear()`     | Delete items     |
# | ⚙️ Modify        | `lst[0] = value`                   | Change item      |
# | 🧮 Sort          | `sort()`, `reverse()`              | Reorder          |
# | 💡 Length        | `len(lst)`                         | Count            |
# | 🔁 Loop          | `for x in lst:`                    | Iterate          |
# | 💫 Comprehension | `[x**2 for x in range(5)]`         | Fast create      |
# | ♻️ Copy          | `copy()`, `list()`                 | Duplicate safely |


fruits = ['apple', 'banana', 'cherry'] # String List
numbers = [1, 2, 3, 4, 5] # Integer List
mixed = [1, 'apple', 3.5, True]  # Mixed List
nested = [[1, 2], [3, 4]] # Nested List
empty = [] # Empty List


# Updating & Changing Items
fruits[1] = 'mango'
print(fruits) # ['apple', 'mango', 'cherry']


# 🧊 Multi-Dimensional Array — 3D or More
cube = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
]
print(cube[1][0][1])  # Output: 6
