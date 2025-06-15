def main():
    from random import uniform; from random import randint; from sys import exit; from time import sleep

    def generate_moves() -> str:
        computer_move = randint(1,3)
        if computer_move == 1:
            return 'rock'
        elif computer_move == 2:
            return 'paper'
        elif computer_move == 3:
            return 'scissors'
    
    def check_move(computer_move, player_move):
        if computer_move == player_move:
            return 'It\'s a tie!'
        elif computer_move == 'rock' and player_move == 'scissors':
            return 'Computer win!'
        elif computer_move == 'paper' and player_move == 'rock':
            return 'Computer win!'
        elif computer_move == 'scissors' and player_move == 'paper':
            return 'Computer win!'
        elif computer_move == 'rock' and player_move == 'paper':
            return 'Player win!'
        elif computer_move == 'paper' and player_move == 'scissors':
            return 'Player win!'
        elif computer_move == 'scissors' and player_move == 'rock':
            return 'Player win!'

    move_list = ['rock', 'scissors', 'paper']
    computer_move = generate_moves()
    player_move = input('\nEnter your move (Rock, Scissors, Paper):')
    while player_move.lower() not in move_list:
        print(f'{player_move} is not a valid move.', end='')
        player_move = input(' Enter Rock, Paper, or Scissors.\n')
    print(f'\n{player_move.upper()} versus...\n\n\n\n')
    sleep(uniform(1, 3))
    print(f'{computer_move.upper()}! ')
    print(f'\n{check_move(computer_move=computer_move, player_move=player_move)}\n')
    exit()

if __name__ == '__main__':
    main()
