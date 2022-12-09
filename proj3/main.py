import random

from conf import GAME_CHOICES, RULES, scorebord


def get_user_choice():
    """
    get and validate player input, recersivel
    """
    user_input = input("Enter your choice please (r, p, s): ")
    if user_input not in GAME_CHOICES:
        print("Oops!!, wrong choice, try again please...")
        return  get_user_choice()
    return user_input

def get_system_choice():
    """
    choice rando from GAME_CHOICE
    """
    return random.choice(GAME_CHOICES)

def find_winner(user, system):
    """
    receive user and system choice, sort them and compare with
    game rules if they are not the same.
    """
    match = {user, system}
    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]

def update_scoreboard(result):
    """
    Update scorbeord after each hand of the game and show live result
    unit now + last hand result
    :param result:
    :return:
    """

    if result['user'] == 3:
        scorebord['user'] += 1
        msg = 'You win'
    else:
        scorebord['system'] += 1
        msg = 'You lose'

    print('#' * 30)
    print('##', f'user: {scorebord["user"]}'.ljust(24), "##")
    print('##', f'system: {scorebord["system"]}'.ljust(24), "##")
    print('#' * 30)

def play():
    """
    Main play ground handler
    """
    result = {'user': 0, 'system': 0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        syste_choice = get_system_choice()
        winner = find_winner(user_choice, syste_choice)
        if winner == user_choice:
            msg = 'You win'
            result['user'] += 1
        elif winner == syste_choice:
            msg = 'You lose'
            result['system'] += 1
        else:
            msg = 'Drow'
        print(f"your choice: {user_choice}\t system: {syste_choice}\t result: {msg}")
        print(result)
    update_scoreboard(result)
    play_again = input("Do you want to play again? (y/n):")
    if play_again == 'y':
        play()

if __name__ == '__main__':
   play()
