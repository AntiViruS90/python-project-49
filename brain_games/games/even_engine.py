import random
from brain_games.game_const import GAME_INSTRUCTIONS
from brain_games.game_engine import run_game


def number_and_even_answer():
    num = random.randint(1, 30)
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    return num, correct_answer


def run_even_engine_game():
    run_game(number_and_even_answer, GAME_INSTRUCTIONS['even'])
