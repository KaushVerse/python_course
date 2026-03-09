"""
File: iterators.py
Topic: Custom Iterators
"""

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1


if __name__ == "__main__":
    countdown = Countdown(5)

    print("🚀 Countdown:")
    for number in countdown:
        print(number)
