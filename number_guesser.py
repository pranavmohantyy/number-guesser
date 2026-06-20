import random
import json
import time

def start_game():
    difficulty = input("Select difficulty (easy, medium, hard, timed): ").lower()
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
    elif difficulty == 'timed':
        number_to_guess = random.randint(1, 100)
        max_attempts = float('inf')
        base_score = 50
        start_time = time.time()
    else:
        print("Invalid difficulty. Defaulting to medium.")
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
        base_score = 70

    score = 0
    attempts = 0
    while attempts < max_attempts:
        if difficulty == 'timed' and (time.time() - start_time) > 30:
            print("Time's up!")
            break
        guess = int(input("Guess the number: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            time_taken = time.time() - start_time if difficulty == 'timed' else 0
            score = base_score - (attempts * 10)
            if difficulty == 'timed':
                score += max(0, int((30 - time_taken) / 30 * base_score))
            print(f"Congratulations! You guessed the number in {attempts} attempts with a score of {score}.")
            break
    else:
        print(f"Sorry, the number was {number_to_guess}. Better luck next time!")

if __name__ == '__main__':
    start_game()