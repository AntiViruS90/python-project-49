import random
from brain_games.game_engine import run_game
from brain_games.game_const import PROGRESSION_LENGTH, GAME_INSTRUCTIONS


def func_progression_and_missed_num():
    start_num, step = random.randint(1, 5), random.randint(1, 5)
    progression = []

    for i in range(PROGRESSION_LENGTH):
        progression.append(start_num + step * i)

    index_missed = random.randint(1, PROGRESSION_LENGTH - 1)
    missed_num = progression[index_missed]
    progression[index_missed] = '..'
    progression_for_player = ' '.join(map(str, progression))
    return progression_for_player, str(missed_num)


def run_func_progression_and_answer():
    run_game(func_progression_and_missed_num, GAME_INSTRUCTIONS['progression'])
