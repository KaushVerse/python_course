"""
File: generators.py
Topic: Generators & yield
"""

def count_up_to(n):
    for i in range(1, n + 1):
        yield i


def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("🔢 Counting:")
    for num in count_up_to(5):
        print(num)

    print("\n🧮 Fibonacci:")
    for num in fibonacci(50):
        print(num)
