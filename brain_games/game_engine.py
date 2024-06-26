import prompt
from brain_games.game_const import ROUND_COUNT, GREETING


def run_game(question_and_answer, instruction_of_game):
    player_name = prompt.string(f"{GREETING} ")
    print(f'Hello, {player_name}!'
          f'\n{instruction_of_game}')

    for _ in range(ROUND_COUNT):
        question, correct_answer = question_and_answer()
        player_answer = prompt.string(f"Question: {question}\n"
                                      f"Answer: ")

        if correct_answer == player_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {player_name}!")
            return

    return print(f"Congratulations, {player_name}!")
