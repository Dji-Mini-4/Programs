def main():
    import random, time
    print('Brainstorming Words, by Jayden\n')
    print('In this game, you will need to give the computer a word. \nEither the computer will give back a word that starts with the last letter of the word you gave, or the computer will give up. Then, you win.')
    print('If you give up, the computer wins the round.')
    print('Alright, let\'s get started!')

    # Use a with statement to handle file reading
    with open('D:\\Setup\\Setup_Files\\all_word_list.txt') as file:
        word_lst = file.read().split('\n')

    # Initialize scores
    player_score = 0
    computer_score = 0

    while True:  # Loop for multiple rounds
        possible_words = []
        word_guessed = []

        print('\nStarting a new round!')
        print(f'Current Scores - Player: {player_score}, Computer: {computer_score}\n')

        while True:
            # Determine the required letter
            if word_guessed:
                required_letter = word_guessed[-1][-1].lower()
                prompt = f'Give the computer a word that starts with "{required_letter}" (or type GIVE UP to forfeit the round, or QUIT to exit): '
            else:
                prompt = 'Give the computer a word (or type GIVE UP to forfeit the round, or QUIT to exit): '

            word = input(prompt).upper()
            if word == 'QUIT':
                print(f'\nFinal Scores - Player: {player_score}, Computer: {computer_score}')
                print('\nThanks for playing! Goodbye!')
                return  # Exit the program
            if word == 'GIVE UP':
                print('\nYou gave up. The computer wins this round!')
                computer_score += 1
                break  # End the current round

            # Check if the word is valid
            while word not in word_lst or word in word_guessed or word in ['I', 'A'] or (word_guessed and word[0] != word_guessed[-1][-1]):
                if word in word_guessed:
                    print('You have already guessed that word.')
                elif word in ['I', 'A']:
                    print('Single-letter words like "I" and "A" are not allowed.')
                elif word_guessed and word[0] != word_guessed[-1][-1]:
                    print(f'That word does not start with the letter "{word_guessed[-1][-1]}".')
                else:
                    print('That is not a valid word.')
                word = input(prompt).upper()
                if word == 'QUIT':
                    print(f'\nFinal Scores - Player: {player_score}, Computer: {computer_score}')
                    print('\nThanks for playing! Goodbye!')
                    return  # Exit the program
                if word == 'GIVE UP':
                    print('\nYou gave up. The computer wins this round!')
                    computer_score += 1
                    break  # End the current round

            if word == 'GIVE UP' or word == 'QUIT':
                break  # Exit the round if the player gives up or quits

            # Add the word to the guessed list
            word_guessed.append(word)

            # Adjust the probability of the computer giving up if the word ends with 'X'
            if word[-1] == 'X' or word[-1] == 'Q' or word[-1] == 'Z' or word[-1] == 'Y':
                computer_choice = random.randint(0, 10)  # Higher chance of giving up
            else:
                computer_choice = random.randint(0, 20)

            print('Alright, let me think...')

            if computer_choice == 5:  # Adjusted probability for giving up
                time.sleep(random.uniform(3.0, 5.0))
                print('I give up. You win this round!')
                player_score += 1
                break  # End the current round
            else:
                possible_words.clear()
                for i in word_lst:
                    if i.startswith(word[-1]) and i not in word_guessed:
                        possible_words.append(i)

                if not possible_words:
                    print('I give up. You win this round!')
                    player_score += 1
                    break  # End the current round

                time.sleep(random.uniform(1.0, 4.0))
                computer_word = random.choice(possible_words).lower()
                print(f'I have thought of a word. It is {computer_word}.')
                word_guessed.append(computer_word.upper())

        # Ask the user if they want to play another round
        play_again = input('\nDo you want to play another round? (yes or no): ').lower()
        if play_again != 'yes':
            print(f'\nFinal Scores - Player: {player_score}, Computer: {computer_score}')
            print('\nThanks for playing! Goodbye!')
            break


if __name__ == '__main__':
    main()
