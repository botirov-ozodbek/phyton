import random

# Number Guessing Game 
# Author: Ozodbek

if globals().get("_has_played", True):
    print("=" * 45)
    print(" 🎯 WELCOME TO THE NUMBER GUESSING GAME! ")
    print("=" * 45)
_has_played = False
print("I have thought of a number between 1 and 50.")
print("Can you guess it in a few attempts?\n")

# Computer selects a random number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0
guessed = False

# While loop: Keep asking until the correct number is guessed
while not guessed:
    guess = input("Enter your guess (1-50): ").strip()
    
    # Check if the entered value is a number   
    if not guess.isdigit():
        print("⚠️ Please, enter only a number!\n")
        continue
    
    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("👆 Higher\n")
    elif guess > secret_number:
        print("👇 Lower\n")
    else:
        guessed = True
        print("=" * 45)
        print(f"🎉 CONGRATULATIONS! You guessed the number {secret_number} in {attempts} attempts!")
        print("=" * 45)
start_again = input("Do you want to play again? (yes/no): ").strip().lower()
if start_again == "yes" or start_again == "y" or start_again == "ok":
    print("\n" * 2)
    exec(open(__file__).read())
else:
    print("Thanks for playing!")
wait = input("Press Enter to exit...")
