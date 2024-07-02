import prompt

ROUND_COUNT = 3


def run(game):
    """
       Run the game with the given game logic.

       The function welcomes the player, asks for their name, displays the game task,
       runs the game for a certain number of rounds, checks player's answers,
       and prints the final result.

       Parameters:
       game (module): The game module containing the logic for the specific game.

       Returns:
       None
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(f"{game.GAME_TASK}")

    for _ in range(ROUND_COUNT):
        (question, correct_answer) = game.question_and_answer()
        print(question)
        player_answer = prompt.string("Answer: ")

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {player_name}!")
            return

    return print(f"Congratulations, {player_name}!")
