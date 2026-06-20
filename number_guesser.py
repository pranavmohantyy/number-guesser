import random

def start_game():
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    if difficulty == 'easy':
        number_to_guess = random.randint(1, 50)
        max_attempts = 10
    elif difficulty == 'medium':
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
    elif difficulty == 'hard':
        number_to_guess = random.randint(1, 200)
        max_attempts = 5
    else:
        print("Invalid difficulty. Defaulting to medium.")
        number_to_guess = random.randint(1, 100)
        max_attempts = 7

    attempts = 0
    while attempts < max_attempts:
        user_guess = int(input("Guess the number: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            return
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == '__main__':
    start_game()