def main():
    from random import choice
    from time import sleep

    print('Welcome to Rock, Paper, Scissors!')
    print('The game will be best out of 3.')
    print('You will be playing against the computer.')
    print('Rock beats scissors, scissors beats paper, and paper beats rock.')
    print('Good luck!')

    def check_moves(computer_move, player_move):
        if computer_move == player_move:
            return 'It\'s a tie!'
        elif computer_move == 'rock' and player_move == 'scissors':
            return 'Computer wins!'
        elif computer_move == 'scissors' and player_move == 'paper':
            return 'Computer wins!'
        elif computer_move == 'paper' and player_move == 'rock':
            return 'Computer wins!'
        else:
            return 'Player wins!'

    def print_results(computer_move, player_move):
        rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
        '''

        paper = '''
        _______
    ---'   ____)___
            ______)
            _______)
            _______)
    ---.__________)
        '''

        scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
        '''

        rock_reversed = '''
        _______
        (____   '---
    (_____)
    (_____)
    (____)
        (___)__.---
        '''

        paper_reversed = '''
        _______
    (____   '---
    (______
    (_______
    (_______
        (__________.---
        '''

        scissors_reversed = '''
        _______
    (____   '---
    (______
    (__________
        (____)
        (___)__.---
        '''

        if player_move == 'rock':
            print(f'Player move: {player_move.upper()}')
            print(rock_reversed)
        elif player_move == 'paper':
            print(f'Player move: {player_move.upper()}')
            print(paper_reversed)
        else:
            print(f'Player move: {player_move.upper()}')
            print(scissors_reversed)
        print('\nVS\n')
        if computer_move == 'rock':
            print(f'Computer move: {computer_move.upper()}')
            print(rock)
        elif computer_move == 'paper':
            print(f'Computer move: {computer_move.upper()}')
            print(paper)
        else:
            print(f'Computer move: {computer_move.upper()}')
            print(scissors)

    moves = ['rock', 'paper', 'scissors']
    score = [0, 0]
    score_limit = 2

    while True:
        while True:
            player_move = input('Enter your move (rock, paper, scissors): ').lower()
            if player_move in moves:
                break
            print('Invalid move. Please enter "rock", "paper", or "scissors".')

        computer_move = choice(moves)
        print('\nThe result is...')
        sleep(1)
        print(f'{player_move.upper()} vs {computer_move.upper()}!\n')
        print_results(computer_move, player_move)

        result = check_moves(computer_move, player_move)
        print(result, '\n')

        if result == 'Player wins!':
            score[1] += 1
        elif result == 'Computer wins!':
            score[0] += 1

        print(f'Computer: {score[0]}')
        print(f'Player: {score[1]}')

        if score[0] == score_limit:
            print('Computer wins the game!\nBetter luck next time!')
            exit()
        elif score[1] == score_limit:
            print('Player wins the game!\nCongratulations!')
            exit()

        user_input = input('Press Enter to continue or type "quit" to exit: ').lower()
        if user_input == 'quit':
            exit()


if __name__ == '__main__':
    main()