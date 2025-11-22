# 🔐 Password Generator
# By Kaushik 🚀

import random
import string

def generate_password(length=12):
    # 🧩 Character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*()_+
    
    # 🎯 Combine all character types
    all_chars = letters + digits + symbols
    
    # 🧠 Ensure strong mix of characters
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill remaining characters
    password += random.choices(all_chars, k=length - 3)
    
    # 🔀 Shuffle for randomness
    random.shuffle(password)
    
    return ''.join(password)

print("🔐 Welcome to the Python Password Generator!")

try:
    length = int(input("📏 Enter password length (min 6 recommended): "))
    if length < 6:
        print("⚠️ Password too short! Setting to 6 by default.")
        length = 6
    print(f"✅ Your strong password is: {generate_password(length)}")
except ValueError:
    print("⚠️ Please enter a valid number!")
