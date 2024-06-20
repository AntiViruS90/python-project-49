import prompt
import random


def even_game():
    player_name = prompt.string("Welcome to the Brain Games!\n"
                                "May I have your name? ")
    print(f'Hello, {player_name}!'
          f'\nAnswer "yes" if the number is even, otherwise answer "no"')

    for _ in range(3):
        num = random.randint(1, 31)
        correct_answer = 'yes' if num % 2 == 0 else 'no'

        player_answer = prompt.string(f'Question: {num}'
                                      f'\nAnswer: ').lower()

        if correct_answer == player_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {player_name}!")

    return print(f"Congratulations, {player_name}!")
