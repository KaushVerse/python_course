# 🧮 Simple Calculator App
# By Kaushik 🚀

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Division by Zero!"
    return x / y

# 🏁 Main Program
print("🧮 Welcome to Python Calculator!")
print("Choose operation:")
print("1️⃣ Add")
print("2️⃣ Subtract")
print("3️⃣ Multiply")
print("4️⃣ Divide")

# 🔹 User Input
choice = input("👉 Enter choice (1/2/3/4): ")

num1 = float(input("🔢 Enter first number: "))
num2 = float(input("🔢 Enter second number: "))

# ⚙️ Perform Operation
if choice == '1':
    print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"✅ Result: {num1} × {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"✅ Result: {num1} ÷ {num2} = {divide(num1, num2)}")
else:
    print("⚠️ Invalid Input!")
