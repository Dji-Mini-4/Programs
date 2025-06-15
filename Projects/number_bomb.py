def main():
    import random, sys

    print('Number Bomb, by Jayden')
    print('You need to guess (input a number) a number every round. Try not to guess the computer\'s number.')
    print('You can select the starting boundary, which will limit your guess.')
    print('You win if the computer\'s number is the only number you can guess. (That is called a "catch")')

    accept_boundaries = [[1, 100], [1, 1000], [1, 10000]]
    wins = 0
    losses = 0

    while True:
        # Display boundary options
        print('\nChoose a boundary:')
        for i, boundary in enumerate(accept_boundaries):
            print(f'{i + 1}: {boundary[0]} to {boundary[1]}')

        # Get the user's boundary choice
        while True:
            try:
                choice = int(input('Enter the number corresponding to your choice (1-3): '))
                if 1 <= choice <= len(accept_boundaries):
                    lower_bound, upper_bound = accept_boundaries[choice - 1]
                    lower_bound, upper_bound = int(lower_bound), int(upper_bound)
                    break
                else:
                    print('Invalid choice. Please select a number between 1 and 3.')
            except ValueError:
                print('Please enter a valid number.')

        # Generate the computer's number
        computer_number = random.randint(lower_bound + 1, upper_bound - 1)
        print(f'\nThe computer has chosen a number between {str(lower_bound)} and {str(upper_bound)}.')

        # Start the game loop
        while lower_bound < upper_bound:
            print(f'\nboundary = {str(lower_bound)} ~ {str(upper_bound)}')
            try:
                guess = int(input(f'Enter your guess ({lower_bound}-{upper_bound}): '))
                if guess <= lower_bound or guess >= upper_bound:
                    print('Invalid guess. You cannot guess the boundary numbers.')
                    continue

                if guess == computer_number:
                    print('\nBOOM! You guessed the computer\'s number. You lose!')
                    losses += 1
                    break
                elif guess > computer_number:
                    upper_bound = guess
                else:
                    lower_bound = guess

                # # Print the updated boundary
                # print(f'New boundary = {str(lower_bound)} ~ {str(upper_bound)}')
            except ValueError:
                print('Please enter a valid number.')

        # Check if the player wins
        if lower_bound == upper_bound:
            print(f'\nCongratulations! You catched the number! The only number left is {computer_number}. You win!')
            wins += 1

        # Display the score
        print(f'Wins: {wins}, Losses: {losses}')

        # Ask if the player wants to play another round
        play_again = input('Do you want to play another round? (yes/no): ').strip().lower()
        if play_again != 'yes':
            print('Thanks for playing Number Bomb! Goodbye!')
            break

if __name__ == '__main__':
    main()