import time
import sys

def type_text(text, speed=0.05):
    """Character-by-character typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # for new line

def sing_song():
    lyrics = [
        "🎵 Jab tak hai jaan, jab tak hai jaan...",
        "Tu mere saath chal...",
        "Chalna hi zindagi hai...",
        "🔥 Dil se dil tak ek raasta...",
        "Aur woh raasta tu ho...",
    ]

    print("\n--- Song Playing... 🎶 ---\n")
    time.sleep(1)

    for line in lyrics:
        type_text(line, speed=0.06)  # typing speed
        time.sleep(0.8)              # delay between lines

    print("\n--- Song Ended 🎧 ---")

if __name__ == "__main__":
    sing_song()
