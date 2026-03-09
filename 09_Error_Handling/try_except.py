"""
File: try_except.py
Topic: Error Handling in Python (Best Practices)
"""

def divide_numbers(a, b):
    try:
        print(f"Trying to divide {a} by {b}")
        result = a / b

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero")

    except TypeError:
        print("❌ Error: Please provide numeric values only")

    except Exception as e:
        # Catch-all for unexpected errors
        print(f"❌ Unexpected error occurred: {e}")

    else:
        # Runs only if no exception occurred
        print(f"✅ Result: {result}")
        return result

    finally:
        # Always runs (cleanup / logging)
        print("🔁 Division operation completed\n")


def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")

    except PermissionError:
        print(f"❌ Error: No permission to read '{filename}'")

    else:
        print("✅ File read successfully")
        return content

    finally:
        print("📁 File operation finished\n")


if __name__ == "__main__":
    # Number division examples
    divide_numbers(10, 2)
    divide_numbers(10, 0)
    divide_numbers(10, "a")

    # File handling example
    read_file("sample.txt")
