import math
import random
from brain_games.game_engine import run_game
from brain_games.game_const import GAME_INSTRUCTIONS


def func_numbers_and_gcd():
    first_num, second_num = random.randint(1, 50), random.randint(1, 30)
    gcd_answer = math.gcd(first_num, second_num)
    numbers = f"{first_num} {second_num}"
    return numbers, str(gcd_answer)


def run_gcd_engine_game():
    run_game(func_numbers_and_gcd, GAME_INSTRUCTIONS['gcd'])
