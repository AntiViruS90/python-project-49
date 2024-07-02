from random import randint, choice


GAME_TASK = 'What is the result of the expression?'
OPERATORS = ["+", "-", "*"]


def calculate(first_num, math_sign, second_num):
    """
        Calculate the result of the arithmetic expression.

        Args:
            first_num (int): The first number in the expression.
            math_sign (str): The arithmetic operator (+, -, *).
            second_num (int): The second number in the expression.

        Returns:
            int: The result of the arithmetic expression.
    """
    result = eval(str(first_num) + math_sign + str(second_num))
    return result


def question_and_answer():
    """
        Generate a math question and calculate the correct answer.

        Returns:
            tuple: A tuple containing the math question and the correct answer.
    """
    first_num, second_num = randint(1, 30), randint(1, 30)
    operator = choice(OPERATORS)

    question = f"Question: {first_num} {operator} {second_num}"
    correct_answer = str(calculate(first_num, operator, second_num))

    return question, correct_answer
