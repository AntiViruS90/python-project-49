import random
import prompt


def math_calc():
    player_name = prompt.string("Welcome to the Brain Games!\n"
                                "May I have your name? ")
    print(f'Hello, {player_name}!'
          f'\nWhat is the result of the expression?')
    for _ in range(3):
        first_num = random.randint(1, 10)
        second_num = random.randint(1, 10)
        calc_sign_list = ["+", "-", "*"]
        calc_sign_random = random.choice(calc_sign_list)
        expression = f"{first_num} {calc_sign_random} {second_num}"
        correct_answer = eval(expression)

        player_answer = prompt.string(f"\nQuestion: {expression}"
                                      f"\nAnswer: ")

        if correct_answer == int(player_answer):
            print("Correct!")
        else:
            print(f"'{player_answer}' is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again, {player_name}!")

    return print(f"Congratulations, {player_name}!")
