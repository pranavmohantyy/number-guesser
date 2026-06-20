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
        guess = int(input(f"Attempt {attempts + 1}: Guess the number: "))
        attempts += 1
        if guess == number_to_guess:
            print(f"Correct! Your score is {score}. ")
            save_score(score)
            return
        else:
            score -= 10
            print("Try again!")

    print(f"Out of attempts! The number was {number_to_guess}.")


def save_score(score):
    try:
        with open('leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = []

    name = input("Enter your name for the leaderboard: ")
    leaderboard.append({"name": name, "score": score})

    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard, f)

if __name__ == '__main__':
    start_game()