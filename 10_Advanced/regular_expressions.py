"""
File: regular_expressions.py
Topic: Regular Expressions (re module)
"""

import re

text = "Contact us at support@gmail.com or sales@company.in"

# 1️⃣ Find emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}", text)
print("📧 Emails found:", emails)

# 2️⃣ Phone number validation
phone = "9876543210"
if re.fullmatch(r"\d{10}", phone):
    print("📞 Valid phone number")
else:
    print("❌ Invalid phone number")

# 3️⃣ Password validation
password = "Admin@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.match(pattern, password):
    print("🔐 Strong password")
else:
    print("❌ Weak password")
