import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """
        Check if a number is prime.

        Args:
            num (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True


def question_and_answer():
    """
        Generate a question and answer for checking if a number is prime.

        Returns:
            tuple: A tuple containing the question and the correct answer.
    """
    num = random.randint(1, 30)

    question = f"Question: {num}"
    correct_answer = 'yes' if is_prime(num) else 'no'

    return question, correct_answer
