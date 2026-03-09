"""
File: raise_custom.py
Topic: Raising Custom Exceptions in Python
"""

# 1️⃣ Custom Exception
class AgeNotValidError(Exception):
    """Raised when age is below required limit"""
    pass


class InsufficientBalanceError(Exception):
    """Raised when account balance is insufficient"""
    pass


# 2️⃣ Functions using custom exceptions
def check_age(age):
    if age < 18:
        raise AgeNotValidError("❌ Age must be 18 or above")
    print("✅ Age verified")


def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            f"❌ Insufficient balance. Available: ₹{balance}"
        )
    print(f"✅ Withdrawal successful. Remaining balance: ₹{balance - amount}")


# 3️⃣ Handling raised exceptions
if __name__ == "__main__":
    # Age validation
    try:
        check_age(16)
    except AgeNotValidError as e:
        print(e)

    print("-" * 41)

    # Bank transaction
    try:
        withdraw_money(5000, 7000)
    except InsufficientBalanceError as e:
        print(e)
    finally:
        print("🔁 Transaction process completed")
