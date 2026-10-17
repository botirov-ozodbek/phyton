

import time

# Welcome to a quiz test!
# There are 10 questions in this quiz. Each question has 4 options, and only one option is correct. You will get 1 point for each correct answer. Let's begin!

print("=" * 40)
print(" WELCOME TO THE IELTS/CEFR VOCAB QUIZ! ")
print("=" * 40)
print("Answer the following vocabulary questions.\n")

score = 0

time.sleep(5)  # Pause for 5 seconds before displaying the first question
# ⏱️ Start the timer
start_time = time.time()

# question 1
print("Question 1: Where is the capital of France?")
print("A) London")
print("B) Berlin")
print("C) Paris")
print("D) Madrid")
answer1 = input("Your answer (a/b/c/d): ").lower().strip()

if answer1 == "c":
    print("✨ Correct! Paris is the capital of France.")
    score += 1
else:
    print("❌ Incorrect! The correct answer is c) Paris.")

# Question 2
print("Question 2: What is the capital of Uzbekistan?")
print("A) Samarqand")
print("B) Tashkent")
print("C) Bukhara")
print("D) Namangan")

answer2 = input("Your answer (a/b/c/d): ").lower().strip()

if answer2 == "b":
    print("✨ Correct! Tashkent is the capital of Uzbekistan.")
    score += 1
else:
    print("❌ Incorrect! The correct answer is b) Tashkent.")

# Question 3
print("Question 3: What is the capital of Japan?")
print("A) Tokyo")
print("B) Kyoto")
print("C) Osaka")
print("D) Hiroshima")

answer3 = input("Your answer (a/b/c/d): ").lower().strip()

if answer3 == "a":
    print("✨ Correct! Tokyo is the capital of Japan.")
    score += 1
else:
    print("❌ Incorrect! The correct answer is a) Tokyo.")

# ⏱️ Stop the timer and calculate total time elapsed
end_time = time.time()
total_time = round(end_time - start_time, 2)

# Final Results
print("=" * 40)
print(f" QUIZ COMPLETED! Your final score: {score}/3 ")
print(f"Total time elapsed: {total_time} seconds")
print("=" * 40)

if score == 3:
    print("🏆 Excellent! You know your academic vocabulary inside out!")
elif score == 2:
    print("👍 Good job! Just a little more practice to reach perfection.")
else:
    print("📚 Keep studying! Review your vocabulary list and try again.")