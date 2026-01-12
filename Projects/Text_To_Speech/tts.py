# 🔊 Text-to-Speech Bot (Offline)
# By Kaushik 🚀

import pyttsx3

engine = pyttsx3.init()

# Voice settings
engine.setProperty("rate", 170)   # Speed
engine.setProperty("volume", 1.0) # Volume (0.0 - 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("🔊 Text-to-Speech Bot Started!")
print("✏️ Type text and press Enter (q to quit)\n")

while True:
    text = input("💬 You: ")

    if text.lower() == "q":
        speak("Goodbye! Have a nice day.")
        break

    speak(text)
