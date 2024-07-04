from math import gcd
from random import randint

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def generate_random_numbers():
    """
       Generate two random numbers within specified ranges.

       Returns:
           tuple: A tuple containing two random numbers generated.
    """
    return randint(1, 50), randint(1, 30)


def get_question_and_answer():
    """
        Generate a question and answer for finding the greatest
        common divisor of two numbers.

        Returns:
            tuple: A tuple containing the question and the correct answer.
    """
    first_num, second_num = generate_random_numbers()

    question = f"Question: {first_num} {second_num}"
    correct_answer = gcd(first_num, second_num)

    return question, str(correct_answer)
