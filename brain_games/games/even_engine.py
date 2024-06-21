import prompt
import random
from brain_games.game_const import GAME_INSTRUCTIONS, ROUND_COUNT, GREETING


def even_game():
    player_name = prompt.string(f"{GREETING} ")
    print(f'Hello, {player_name}!'
          f'\n{GAME_INSTRUCTIONS["even"]}')

    for _ in range(ROUND_COUNT):
        num = random.randint(1, 31)
        correct_answer = 'yes' if num % 2 == 0 else 'no'

        player_answer = prompt.string(f'Question: {num}'
                                      f'\nAnswer: ').lower()

        if correct_answer == player_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {player_name}!")

    return print(f"Congratulations, {player_name}!")
