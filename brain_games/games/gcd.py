from math import gcd
from random import randint

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    first_num, second_num = randint(1, 50), randint(1, 30)

    question = f"Question: {first_num} {second_num}"
    correct_answer = gcd(first_num, second_num)

    return question, str(correct_answer)
