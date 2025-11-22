# 📖 Tuple ek ordered, immutable (unchangeable) collection hoti hai jisme multiple items store kar sakte ho — just like a list

my_tuple = (10, 20, 30)
print("Original Tuple:", my_tuple)

# ⚙️ Key Features (with Icons)

# | ⚙️ Feature           | 📖 Description                    |
# | -------------------- | --------------------------------- |
# | 🧱 **Immutable**     | Once created, can’t change values |
# | 📦 **Ordered**       | Keeps insertion order             |
# | 🔢 **Indexed**       | Access elements by index          |
# | 🌈 **Heterogeneous** | Can hold multiple data types      |
# | ⚡ **Faster**         | Tuples are faster than lists      |


# 🧾 Summary Table (Cheat Sheet with Icons)

# | 📦 Concept     | 🧠 Description                | 💡 Example          |
# | -------------- | ----------------------------- | ------------------- |
# | ✨ Create       | `(1,2,3)` or `tuple([1,2,3])` | Define tuple        |
# | 🎯 Index       | `t[0]`, `t[-1]`               | Access item         |
# | ✂️ Slice       | `t[1:3]`                      | Extract part        |
# | 🚫 Immutable   | No modification               | `t[0]=5 ❌`          |
# | ➕ Add / Repeat | `t1 + t2`, `t*2`              | Combine             |
# | 🧮 Methods     | `count()`, `index()`          | Basic tools         |
# | 🔁 Iterate     | `for x in t:`                 | Loop                |
# | 🧱 Unpack      | `a,b,c = t`                   | Assign values       |
# | ⚡ Fast         | Less memory, fast access      | Performance boost   |
# | 🔐 Hashable    | Can be dict key               | Immutable advantage |

# 🔗 Tuple as Dictionary Key

coords = {(1,2): "Point A", (3,4): "Point B"}
print(coords[(1,2)])   # Point A

# 💫 Tuple Comprehension?

t = tuple(x**2 for x in range(5))
print(t)
# (0, 1, 4, 9, 16)
