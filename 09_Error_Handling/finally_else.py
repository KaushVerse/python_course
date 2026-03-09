"""
File: finally_else.py
Topic: try-except-else-finally in Python
"""

def safe_division(a, b):
    try:
        print("🔹 Performing division")
        result = a / b

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero")

    except TypeError:
        print("❌ Error: Inputs must be numbers")

    else:
        # Runs ONLY if no exception occurred
        print("✅ Division successful")
        print(f"Result: {result}")
        return result

    finally:
        # Runs ALWAYS (error ho ya na ho)
        print("🔁 Execution completed\n")


def read_file_safe(filename):
    try:
        file = open(filename, "r")
        content = file.read()

    except FileNotFoundError:
        print(f"❌ File '{filename}' not found")

    else:
        print("✅ File read successfully")
        return content

    finally:
        # Resource cleanup
        try:
            file.close()
            print("📁 File closed safely\n")
        except Exception:
            print("⚠️ No file to close\n")


if __name__ == "__main__":
    # Example 1: else + finally
    safe_division(20, 4)
    safe_division(10, 0)

    # Example 2: file handling
    read_file_safe("demo.txt")
    
    print("🔁 Execution completed\n")
