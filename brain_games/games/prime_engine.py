import random
import prompt
from brain_games.game_const import ROUND_COUNT, GREETING, GAME_INSTRUCTIONS


def func_prime():
    player_name = prompt.string(f"{GREETING} ")
    print(f"Hello, {player_name}!"
          f"\n{GAME_INSTRUCTIONS['prime']}")

    for _ in range(ROUND_COUNT):
        prime_num = random.randint(1, 30)

        correct_answer = 'no' if prime_num <= 1 or any(
            prime_num % i == 0 for i in range(2, (prime_num // 2 + 1))
        ) else 'yes'

        player_answer = prompt.string(f"\nQuestion: {prime_num}"
                                      f"\nAnswer: ")

        if correct_answer == player_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {player_name}!")
            return

    return print(f"Congratulations, {player_name}!")
