import random

def start_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        user_guess = int(input("Guess the number (1-100): "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            break

if __name__ == '__main__':
    start_game()