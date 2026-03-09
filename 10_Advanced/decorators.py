"""
File: decorators.py
Topic: Function Decorators
"""

import time
from functools import wraps


def timer(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def auth_required(func):
    """Decorator for authentication check"""
    @wraps(func)
    def wrapper(user):
        if user != "admin":
            print("❌ Access denied")
            return
        return func(user)
    return wrapper


@timer
def heavy_task():
    time.sleep(1)
    print("✅ Heavy task completed")


@auth_required
def dashboard(user):
    print(f"✅ Welcome to dashboard, {user}")


if __name__ == "__main__":
    heavy_task()
    dashboard("guest")
    dashboard("admin")
