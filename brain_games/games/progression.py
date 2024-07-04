from random import randint

GAME_TASK = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def generate_progression(start_num, step, length):
    """
    Generate an arithmetic progression.

    Args:
        start_num (int): The starting number of the progression.
        step (int): The common difference between numbers in the progression
        length (int): The length of the progression.

    Returns:
        list: A list containing the arithmetic progression.
    """
    progression = [start_num + step * i for i in range(length)]
    return progression


def get_question_and_answer():
    """
        Generate a question and answer for the missing number in
        an arithmetic progression.

        Returns:
            tuple: A tuple containing the question and the correct answer
    """
    start_num, step = randint(1, 5), randint(1, 5)
    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)

    index_missed = randint(1, PROGRESSION_LENGTH - 1)

    correct_answer = progression[index_missed]

    progression[index_missed] = '..'

    question = f"Question: {' '.join(map(str, progression))}"

    return question, str(correct_answer)
