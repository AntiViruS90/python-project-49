import random
from brain_games.game_const import GAME_INSTRUCTIONS, OPERATORS
from brain_games.game_engine import run_game


def math_expression_and_result():
    first_num, second_num = random.randint(1, 10), random.randint(1, 10)
    operator = random.choice(OPERATORS)
    expression = f"{first_num} {operator} {second_num}"
    result = eval(expression)
    return expression, str(result)


def run_calc_engine_game():
    run_game(math_expression_and_result, GAME_INSTRUCTIONS['calc'])
