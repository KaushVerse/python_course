# 📊 Student Grade Tracker
# By Kaushik 🚀

import pandas as pd

students = {}

def add_student():
    name = input("👩‍🎓 Enter student name: ").capitalize()
    subjects = int(input("📚 How many subjects? "))
    marks = {}

    for _ in range(subjects):
        subject = input("🧾 Subject name: ").capitalize()
        score = float(input(f"🔢 Marks in {subject}: "))
        marks[subject] = score

    students[name] = marks
    print(f"✅ {name}'s data added successfully!\n")

def calculate_grade(average):
    if average >= 90:
        return "A+ 🏅"
    elif average >= 80:
        return "A 🌟"
    elif average >= 70:
        return "B 👍"
    elif average >= 60:
        return "C 🙂"
    elif average >= 50:
        return "D ⚠️"
    else:
        return "F ❌"

def view_report():
    if not students:
        print("⚠️ No student data available!\n")
        return

    for name, marks in students.items():
        total = sum(marks.values())
        avg = total / len(marks)
        grade = calculate_grade(avg)

        print(f"\n📄 Report for {name}:")
        for subject, score in marks.items():
            print(f"   📘 {subject}: {score}")
        print(f"📊 Average: {avg:.2f}")
        print(f"🎯 Grade: {grade}\n")

def export_to_csv():
    if not students:
        print("⚠️ No data to export!\n")
        return
    df = pd.DataFrame(students).T.fillna(0)
    df.to_csv("student_grades.csv")
    print("💾 Data exported to student_grades.csv successfully!\n")

def main():
    while True:
        print("🏫 Student Grade Tracker Menu:")
        print("1️⃣ Add Student Data")
        print("2️⃣ View All Reports")
        print("3️⃣ Export to CSV")
        print("4️⃣ Exit")

        choice = input("👉 Choose an option (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_report()
        elif choice == "3":
            export_to_csv()
        elif choice == "4":
            print("👋 Goodbye! Have a great day!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
