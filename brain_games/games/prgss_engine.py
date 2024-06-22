import random
import prompt
from brain_games.game_const import PROGRESSION_LENGTH, GREETING, GAME_INSTRUCTIONS, ROUND_COUNT


def func_progression():
    player_name = prompt.string(f"{GREETING} ")
    print(f"Hello, {player_name}!"
          f"\n{GAME_INSTRUCTIONS['progression']}")

    for _ in range(ROUND_COUNT):
        progression = []

        start_num, step = random.randint(1, 5), random.randint(1, 5)
        for i in range(PROGRESSION_LENGTH):
            progression.append(start_num + step * i)

        index_missed = random.randint(1, PROGRESSION_LENGTH - 1)
        missed_num = progression[index_missed]
        progression[index_missed] = '...'
        progression_for_player = ' '.join(map(str, progression))

        player_answer = prompt.string(f"\nQuestion: {progression_for_player}"
                                      f"\nAnswer: ")

        if missed_num == int(player_answer):
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was {missed_num}.\n"
                  f"Let's try again, {player_name}!")
            return

    return print(f"Congratulations, {player_name}!")
