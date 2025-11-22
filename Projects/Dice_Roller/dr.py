# 🎲 Dice Roller Simulator
# By Kaushik 🚀

import random

def roll_dice():
    dice_value = random.randint(1, 6)
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    return dice_value, dice_faces[dice_value]

print("🎲 Welcome to the Python Dice Roller! 🎲")

while True:
    roll = input("🎯 Press ENTER to roll the dice or type 'q' to quit: ").lower()
    if roll == 'q':
        print("👋 Thanks for playing!")
        break
    value, face = roll_dice()
    print(f"🎰 You rolled a {value}! {face}\n")
