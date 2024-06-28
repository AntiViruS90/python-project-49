import random

GAME_TASK = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def question_and_answer():
    start_num, step = random.randint(1, 5), random.randint(1, 5)
    progression = []

    for i in range(PROGRESSION_LENGTH):
        progression.append(start_num + step * i)

    index_missed = random.randint(1, PROGRESSION_LENGTH - 1)

    correct_answer = progression[index_missed]

    progression[index_missed] = '..'

    question = f"Question: {' '.join(map(str, progression))}"

    return question, str(correct_answer)
