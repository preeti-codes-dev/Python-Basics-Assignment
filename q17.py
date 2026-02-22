# Q17: Number Guessing Game  

# Logic:
# 1. Import random module to generate a random number.
# 2. Ask the user to select a difficulty level.
# 3. Based on the selected level:
#    - Easy  -> generate number between 1 and 50.
#    - Medium -> generate number between 1 and 100.
#    - Hard -> generate number between 1 and 1000.
# 4. If user enters invalid choice, stop the program.
# 5. After setting the secret number, ask the user to start guessing.
# 6. Use a while True loop so the game continues until correct guess.
# 7. If guess is greater than secret number:
#    - Print "Too high".
# 8. If guess is less than secret number:
#    - Print "Too low".
# 9. If guess is equal to secret number:
#    - Print success message.
#    - Break the loop to end the game.


import random

print("Select Difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-1000)")

level = int(input("Enter choice: "))

if level == 1:
    secret_number = random.randint(1, 50)
elif level == 2:
    secret_number = random.randint(1, 100)
elif level == 3:
    secret_number = random.randint(1, 1000)
else:
    print("Invalid choice")
    exit()

print("Start guessing!")

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct! You guessed the number.")
        break