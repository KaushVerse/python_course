# 📧 Email Slicer
# By Kaushik 🚀

def email_slicer():
    print("📧 Welcome to Email Slicer Tool!")
    while True:
        email = input("✉️ Enter your email address (or 'q' to quit): ").strip()
        if email.lower() == 'q':
            print("👋 Exiting Email Slicer!")
            break

        if "@" in email and "." in email:
            username = email.split("@")[0]
            domain = email.split("@")[1]
            domain_name = domain.split(".")[0]
            
            print(f"\n👤 Username: {username}")
            print(f"🏢 Domain: {domain}")
            print(f"🌐 Domain Provider: {domain_name.capitalize()}\n")
        else:
            print("⚠️ Invalid email format! Try again.\n")

if __name__ == "__main__":
    email_slicer()
