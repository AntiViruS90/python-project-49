import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


def question_and_answer():
    num = random.randint(1, 30)

    question = f"Question: {num}"
    correct_answer = 'yes' if is_prime(num) else 'no'

    return question, correct_answer
