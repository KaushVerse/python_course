# 📅 Age Calculator
# By Kaushik 🚀

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    # Adjust if birthday hasn't come yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

print("🎉 Welcome to the Age Calculator! 🎉")
b_date = input("📆 Enter your birthdate (DD-MM-YYYY): ")

try:
    birth_date = datetime.strptime(b_date, "%d-%m-%Y")
    age = calculate_age(birth_date)
    print(f"🧮 You are {age} years old!")
except ValueError:
    print("⚠️ Invalid date format! Please use DD-MM-YYYY.")
