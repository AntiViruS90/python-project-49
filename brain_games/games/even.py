from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def question_and_answer():
    num = randint(1, 30)
    question = f"Question: {num}"
    correct_answer = 'yes' if is_even(num) else 'no'
    return question, correct_answer
