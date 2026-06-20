import random
import json

def start_game():
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    if difficulty == 'easy':
        number_to_guess = random.randint(1, 50)
        max_attempts = 10
        base_score = 100
    elif difficulty == 'medium':
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
        base_score = 70
    elif difficulty == 'hard':
        number_to_guess = random.randint(1, 200)
        max_attempts = 5
        base_score = 50
    else:
        print("Invalid difficulty. Defaulting to medium.")
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
        base_score = 70

    attempts = 0
    score = base_score

    while attempts < max_attempts:
        guess = int(input(f"Guess the number (1-{number_to_guess}): "))
        attempts += 1
        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            return
        score -= base_score // max_attempts

    print(f"Sorry, you've used all attempts. The number was {number_to_guess}.")


def reverse_mode():
    print("Think of a number between 1 and 200.")
    low, high = 1, 200
    attempts = 0
    while True:
        attempts += 1
        guess = (low + high) // 2
        response = input(f"Is your number {guess}? (higher/lower/correct): ").lower()
        if response == 'higher':
            low = guess + 1
        elif response == 'lower':
            high = guess - 1
        elif response == 'correct':
            print(f"The computer guessed your number {guess} in {attempts} attempts!")
            return
        else:
            print("Please respond with 'higher', 'lower', or 'correct'.")


if __name__ == '__main__':
    mode = input("Choose mode (normal/reverse): ").lower()
    if mode == 'reverse':
        reverse_mode()
    else:
        start_game()