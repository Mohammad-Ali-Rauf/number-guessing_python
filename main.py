import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 attempts to guess the correct number.")
    print("Let's begin!\n")

    secret_number = random.randint(1, 100)
    attempts = 5

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            return

        if guess < secret_number:
            print("Incorrect guess. The number is higher.")
        else:
            print("Incorrect guess. The number is lower.")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.\n")
        else:
            print("Sorry, you have run out of attempts.")
            print(f"The correct number was {secret_number}.\n")

    print("Game over!")

guess_number()
