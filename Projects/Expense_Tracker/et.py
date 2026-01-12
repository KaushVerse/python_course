# 📈 Expense Tracker
# By Kaushik 🚀

import pandas as pd
import os
import time

FILENAME = "expenses.csv"

# 🧾 Initialize CSV if it doesn't exist
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Type", "Note"])
    df.to_csv(FILENAME, index=False)

def add_expense():
    date = input("📅 Enter date (DD-MM-YYYY): ")
    category = input("🏷️ Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("💵 Enter amount: "))
    t_type = input("💰 Type (Income/Expense): ").capitalize()
    note = input("📝 Enter short note: ")

    new_data = pd.DataFrame([[date, category, amount, t_type, note]], 
                            columns=["Date", "Category", "Amount", "Type", "Note"])
    new_data.to_csv(FILENAME, mode='a', header=False, index=False)
    print("✅ Transaction saved successfully!")

def view_all():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("📂 No transactions found!")
    else:
        print("\n📊 All Transactions:\n", df)
        print("\n💰 Total Income:", df[df['Type'] == 'Income']['Amount'].sum())
        print("💸 Total Expense:", df[df['Type'] == 'Expense']['Amount'].sum())
        print("📉 Balance:", 
              df[df['Type'] == 'Income']['Amount'].sum() - 
              df[df['Type'] == 'Expense']['Amount'].sum())

def filter_by_category():
    df = pd.read_csv(FILENAME)
    category = input("🏷️ Enter category to filter: ").capitalize()
    filtered = df[df['Category'].str.capitalize() == category]
    if filtered.empty:
        print("⚠️ No data found for this category!")
    else:
        print(filtered)

def delete_all():
    confirm = input("⚠️ Are you sure you want to clear all data? (y/n): ").lower()
    if confirm == 'y':
        pd.DataFrame(columns=["Date", "Category", "Amount", "Type", "Note"]).to_csv(FILENAME, index=False)
        print("🧹 All records cleared!")

def main():
    while True:
        print("\n💸 Expense Tracker Menu:")
        print("1️⃣ Add Transaction")
        print("2️⃣ View All")
        print("3️⃣ Filter by Category")
        print("4️⃣ Clear All")
        print("5️⃣ Exit")

        choice = input("👉 Choose (1–5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            delete_all()
        elif choice == '5':
            print("👋 Thanks for using Expense Tracker!")
            break
        else:
            print("⚠️ Invalid choice!")
        time.sleep(1)

if __name__ == "__main__":
    main()
