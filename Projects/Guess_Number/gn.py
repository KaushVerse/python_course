# 🎯 Guess the Number Game
# By Kaushik 🚀

import random
import time

def guess_the_number():
    print("🎯 Welcome to Guess the Number Game!")
    print("🤖 I'm thinking of a number between 1 and 100...")
    time.sleep(1)

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🏆 Congratulations! You guessed it in {attempts} attempts! 🎉")
                break

        except ValueError:
            print("⚠️ Please enter a valid number!")

def main():
    while True:
        guess_the_number()
        play_again = input("\n🔁 Play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
