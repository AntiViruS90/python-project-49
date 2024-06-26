import random
from brain_games.game_engine import run_game
from brain_games.game_const import GAME_INSTRUCTIONS


def func_prime(num):
    prime_number = 'no' if num <= 1 or any(
        num % i == 0 for i in range(2, (num // 2 + 1))
    ) else 'yes'
    return prime_number


def get_prime_num_and_answer():
    num = random.randint(1, 30)
    prime = func_prime(num)
    return num, prime


def run_prime_engine_game():
    run_game(get_prime_num_and_answer, GAME_INSTRUCTIONS['prime'])
