def main():
    try:
        import keyboard  # type: ignore
    except ModuleNotFoundError:
        print('This program requires the Keyboard module be installed. Open your Terminal and type "py -m pip install keyboard".')
        return
    import random, time

    # ASCII art for realistic hands
    HANDS = {
        "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        """,
        "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
        """,
        "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        """
    }

    print('Rock Paper Scissors 2 Hands Version, by Jayden')
    print('Rules:')
    print('1. Rock beats Scissors')
    print('2. Scissors beats Paper')
    print('3. Paper beats Rock')
    print('You will be entering the moves of your two hands.')
    print('Enter "rock" for Rock, "scissors" for Scissors, and "paper" for Paper.')
    print('After you\'ve entered your moves, the computer will randomly generate its moves.')
    print('When you have seen the computer\'s moves, you have 3 seconds to press either 1 or 2 to choose the hand you want to take away. (just press, DO NOT PRESS ENTER.)')
    print('If you don\'t press any key, the computer will randomly take away one of your hands.')
    print('The winner will be determined based on the moves of the remaining hands.')

    while True:
        def check_move(player_move, computer_move):
            if computer_move == player_move:
                return 'It\'s a tie!', 0
            elif computer_move == 'ROCK' and player_move == 'SCISSORS':
                return 'Computer wins! Bad luck!', 1
            elif computer_move == 'PAPER' and player_move == 'ROCK':
                return 'Computer wins! Bad luck!', 1
            elif computer_move == 'SCISSORS' and player_move == 'PAPER':
                return 'Computer wins! Bad luck!', 1
            else:
                return 'Player wins! You\'re awesome!', 2
        score = [0, 0]
        player_move = list(input('Enter your moves (e.g., rock paper): ').split())
        computer_move = []
        for i in range(2):
            computer_move.append(random.choice(['rock', 'paper', 'scissors']))
        while len(player_move) != 2 or player_move[0] not in HANDS or player_move[1] not in HANDS:
            print('Invalid input. Please enter two valid moves.')
            player_move = list(input('Enter your moves (e.g., rock paper): ').lower())
        p_move_1 = HANDS[player_move[0]]
        p_move_2 = HANDS[player_move[1]]
        c_move_1 = HANDS[computer_move[0]]
        c_move_2 = HANDS[computer_move[1]]
        print('The result is...\n')
        print(f'{player_move[0]} and {player_move[1]}\nVS\n{computer_move[0]} and {computer_move[1]}!')
        print(f'\nPLAYER:\n{p_move_1}\n{p_move_2}\nVS\nCOMPUTER:\n{c_move_1}\n{c_move_2}\n')
        print('MINUS 1! You now have 5 seconds to either press 1 or 2.\npress 1 to take away upper hand, and press 2 to take away lower hand. DO NOT PRESS ENTER.\n')
        for i in range(5):
            print(f'{5 - i}', end='')
            time.sleep(1)
            print('\b')
        time_before = time.time()
        minus_lst = []
        while True:
            time_now = time.time()
            key_pressed_1 = keyboard.is_pressed('1')
            key_pressed_2 = keyboard.is_pressed('2')
            if key_pressed_1 and not key_pressed_2:
                minus_lst.append(0)
                break
            elif key_pressed_2 and not key_pressed_1:
                minus_lst.append(1)
                break
            elif time.time() - time_now == 5:
                break
        if len(minus_lst) == 0:
            minus_lst.append(random.randint(0, 1))
            print('You haven\'t pressed 1 or 2 in 3 seconds. The computer will randomly take away either of your hands.')
        minus_lst.append(random.randint(0, 1))
        if minus_lst[0] == 0:
            del p_move_1; del player_move[0]; str(player_move).upper()
            p_move = p_move_2
        else:
            del p_move_2; del player_move[1]; str(player_move).upper()
            p_move = p_move_1
        if minus_lst[1] == 0:
            del c_move_1; del computer_move[0]; str(computer_move).upper()
            c_move = c_move_2
        else:
            del c_move_2; del computer_move[1]; str(computer_move).upper()
            c_move = c_move_1
        print('\n'*400) # 'clear' the screen
        print(f'{str(player_move)}\nVS\n{str(computer_move)}\nPLAYER:\n{p_move}\nVS\nCOMPUTER:\n{c_move}')
        result = check_move(player_move, computer_move)[0]
        winner = check_move(player_move, computer_move)[1]
        print(f'{result}\n')
        if winner == 1:
            score[0] += 1
        elif winner == 2:
            score[1] += 1
        else:
            pass
        print('Press Enter to continue, or QUIT to quit...'); quit = input()
        if quit.upper() == 'QUIT':
            print(f'The final results is:\nCOMPUTER: {score[0]}\nPLAYER: {score[1]}')
            print('Thanks for playing!')
            return
        elif quit.upper() == '':
            continue
        else:
            while quit.upper() != 'QUIT' or quit.upper() != '':
                print('Invalid input. Press Enter to continue, or QUIT to quit...')
                quit = input()
            if quit.upper() == 'QUIT':
                return

if __name__ == '__main__':
    main()
