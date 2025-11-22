# 📖 Set ek unordered, mutable, aur unique elements ka collection hota hai. Yaani — duplicates automatically remove ho jaate hain 🚫

# ⚙️ Key Features (with Icons)

# | ⚙️ Feature                     | 📖 Description                        |
# | ------------------------------ | ------------------------------------- |
# | 🧱 **Unordered**               | No fixed index or order               |
# | ⚡ **Mutable**                  | You can add/remove items              |
# | 🔑 **Unique Items**            | Duplicates automatically removed      |
# | 💨 **Fast Lookup**             | Membership check is O(1)              |
# | 🔣 **Supports Set Operations** | Union, Intersection, Difference, etc. |

myset = {1, 2, 3, 4}
print(type(myset))


# 🧊 Frozen Set (Immutable Set)

fs = frozenset([1,2,3])
fs.add(4)  # ❌ Error
print(fs)


# ⚡ Set Comprehension

squares = {x*x for x in range(5)}
print(squares)
