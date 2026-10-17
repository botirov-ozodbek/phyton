# Academic Study Planner & Daily Tracker
# Author: Ozodbek
# Project: Python Goal Tracker for CS & IELTS Prep

print("=" * 45)
print(" 📚 DAILY ACADEMIC STUDY TRACKER ")
print("=" * 45)

parol = input("Enter your password(name): ").strip()
if parol == "ozodbek":
    print("You can access the system")
elif parol == "azizbek":
    print("You can access the system")
elif parol == "asilbek":
    print("You can access the system")
else:
    print("Password not found! Exiting the program...")
    exit()
print(f"\nHello, {parol}! Today's study goals are set.\n")

# Vazifalar holatini belgilash (1 = Bajarildi, 0 = Bajarilmadi)
print("📌 Today's Tasks:")
print("1. IELTS/CEFR Writing an essay")
print("2. training IELTS Speaking through YouTube")
print("3. Python coding and GitHub commit")

print("\nFor each task: [1] Completed / [0] Not Completed\n")

task1 = input("was the first task completed ? (1/0): ").strip()
task2 = input("was the second task completed ? (1/0): ").strip()
task3 = input("was the third task completed ? (1/0): ").strip()

completed = 0

if task1 == "yes" or task1 == "1":
    completed += 1
if task2 == "yes" or task2 == "1":
    completed += 1
if task3 == "yes" or task3 == "1":
    completed += 1

# Bajarilgan foizni hisoblash
percentage = round((completed / 3) * 100, 1)

print("\n" + "=" * 45)
print(f" 📊 Result: from 3 tasks, {completed} were completed ({percentage}%)")
print("=" * 45)

if percentage == 100:
    print("🏆 Awesome! Today was 100% productive. You're on track to achieve your goals!")
elif percentage >= 66:
    print("👍 Good job! Most of your tasks were completed successfully.")
elif percentage >= 33:
    print("⚡ Not bad, but let's aim higher tomorrow!")
else:
    print("😴 Looks like you need more rest. Let's tackle everything tomorrow!")