# 🧠 What is Import?
# import ka matlab hai — Python me dusre file, module, ya package ka code apne file me use karna.
# Matlab — “Code likho ek jagah, use karo kahi bhi” 🔥

# 🧱 Import Keywords (with Icons)

# | 🔤 Keyword       | 💡 Meaning                           |
# | ----------------|-------------------------------------- |
# | 📦 import      | Pure module import                     |
# | 🎯 from       | Specific part import                   |
# | 🏷️ as        | Alias/short name dena                  |
# | ➕ import * | All members import (NOT recommended ❌) |


# 🧑‍🏫 Examples
# 1. Pure Module Import 📦
import math

print("Square root of 16 is:", math.sqrt(16))

# 🏷️ Import With Alias
import math as m

print(m.pi)


# 🎯 From Import (Specific Members)
from math import sqrt
from utils.helper import add

print(sqrt(25))

# Using the imported add function from utils.helper module
print(add(5, 10))


# 🎭 Import Multiple Members
from math import sqrt, pi, cos

print("Cosine of 0 is:", cos(0))
print("Value of Pi is:", pi)
print("Square root of 36 is:", sqrt(36))


# ⚠️ Wildcard Import (NOT Recommended)
from math import *


