import random
import prompt
from math import gcd
from brain_games.game_const import GAME_INSTRUCTIONS, ROUND_COUNT, GREETING


def func_gcd():
    player_name = prompt.string(f"{GREETING} ")
    print(f"Hello, {player_name}!"
          f"\n{GAME_INSTRUCTIONS['gcd']}")
    for _ in range(ROUND_COUNT):
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 55)

        correct_answer = gcd(first_num, second_num)

        player_answer = prompt.string(f"\nQuestion: {first_num} {second_num}"
                                      f"\nAnswer: ")

        if correct_answer == int(player_answer):
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was {correct_answer}.\n"
                  f"Let's try again, {player_name}!")
            return

    return print(f"Congratulations, {player_name}!")
