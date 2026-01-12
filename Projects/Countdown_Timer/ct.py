# 🕒 Countdown Timer
# By Kaushik 🚀

import time
import os

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(f"\r⏳ Time Left: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n🎉 Time’s Up!")

def main():
    print("🕒 Welcome to Python Countdown Timer!")
    while True:
        try:
            t = int(input("⏰ Enter time in seconds (or 0 to quit): "))
            if t == 0:
                print("👋 Goodbye!")
                break
            countdown_timer(t)
        except ValueError:
            print("⚠️ Please enter a valid number!")

if __name__ == "__main__":
    main()
