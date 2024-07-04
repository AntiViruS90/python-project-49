from random import randint


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """
        Check if a number is even.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0


def get_question_and_answer():
    """
       Generate a question based on whether a number is even or not.

       Returns:
           tuple: A tuple containing the question and the correct answer.
    """
    num = randint(1, 30)
    question = f"Question: {num}"
    correct_answer = 'yes' if is_even(num) else 'no'
    return question, correct_answer
