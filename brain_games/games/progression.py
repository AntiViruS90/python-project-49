from random import randint

GAME_TASK = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def generate_progression(start_num, step, length):
    progression = [start_num + step * i for i in range(length)]
    return progression


def question_and_answer():
    start_num, step = randint(1, 5), randint(1, 5)
    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)

    index_missed = randint(1, PROGRESSION_LENGTH - 1)

    correct_answer = progression[index_missed]

    progression[index_missed] = '..'

    question = f"Question: {' '.join(map(str, progression))}"

    return question, str(correct_answer)
