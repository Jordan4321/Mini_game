# Game in python terminal
def game():

    x = input(f'Player 1, put your name: ')
    y = input(f'Player 2, put your name: ')
    player1 = x
    player2 = y
    print(f'Welcome, {player1}!!')
    print(f'Welcome, {player2}!!')
    player1_points = 0
    player2_points = 0
    play = True
    while play is True:
        choice1 = input(f'Please write you choice {player1} (scissor, paper or rock): ')
        choice2 = input(f'Please write you choice {player2} (scissor, paper or rock): ')
        choice_list = ['scissor', 'paper', 'rock']
        choice = {'scissor': 1, 'paper': 2, 'rock': 3}
        while True:
            if choice1 in choice_list:
                break
            else:
                choice1 = input(f'Please again write you choice {player1} (scissor, paper or rock): ')
        while True:
            if choice2 in choice_list:
                break
            else:
                choice2 = input(f'Please again write you choice {player2} (scissor, paper or rock): ')
        player1_choice = choice[f'{choice1}']
        player2_choice = choice[f'{choice2}']
        print(f'{player1}, choice: {choice1}!!')
        print(f'{player2}, choice: {choice2}!!')
        if player1_choice == player2_choice:
            print('Draw')
        elif player1_choice == 1 and player2_choice == 2 or player1_choice == 2 \
                and player2_choice == 3 or player1_choice == 3 and player2_choice == 1:
            player1_points += 1
            print(f'{player1}, WIN!')
        elif player1_choice == 1 and player2_choice == 3 or player1_choice == 2 \
                and player2_choice == 1 or player1_choice == 3 and player2_choice == 2:
            player2_points += 1
            print(f'{player2}, WIN!')
        print(f'{player1}:{player1_points} vs {player2}: {player2_points}')
        play_again = input("Play one more time? (y/n): ")
        while True:
            if play_again.lower() == "n":
                print("Bye Bye!")
                play = False
                break
            elif play_again.lower() == "y":
                break
            else:
                play_again = input("Play one more time? (y/n): ")


if __name__ == '__main__':
    game()
