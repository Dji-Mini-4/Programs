def main():
    import random

    def get_greet(guesses: int) -> str:
        if guesses == 10:
            return 'So easy!'
        elif guesses == 9:
            return 'Fantastic!'
        elif guesses == 8:
            return 'Incredible!'
        elif guesses == 7:
            return 'Brilliant!'
        elif guesses == 6:
            return 'Awesome!'
        elif guesses == 5:
            return 'Great!'
        elif guesses == 4:
            return 'Good job!'
        elif guesses == 3:
            return 'Nice!'
        elif guesses == 2:
            return 'Just in time!'
        elif guesses == 1:
            return 'Phew! That was close!'

    def play_again(score: int) -> bool:
        while True:
            user_input = input('Would you like to play again to earn scores? (Y/N): ').upper()
            if user_input == 'Y':
                return True
            elif user_input == 'N':
                print(f'Your final score is {score}.')
                print('Thanks for playing! Goodbye!')
                return False
            else:
                print('Invalid input. Please enter Y or N.')

    # Prompt the user for the desired word length
    while True:
        try:
            word_length = int(input('Enter the desired word length (4-7): '))
            if 4 <= word_length <= 7:
                break
            else:
                print('Invalid input. Please enter a number between 4 and 7.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

    # Prompt the user for the difficulty level
    while True:
        difficulty = input('Choose a difficulty (easy, normal, hard, super hard): ').lower()
        if difficulty == 'easy':
            max_guesses = 10
            break
        elif difficulty == 'normal':
            max_guesses = 8
            break
        elif difficulty == 'hard':
            max_guesses = 6
            break
        elif difficulty == 'super hard':
            max_guesses = 5
            break
        else:
            print('Invalid input. Please choose from easy, normal, hard, or super hard.')

    # Load the word list and filter by the desired word length
    with open('D:\\Setup\\Setup_Files\\all_word_list.txt') as file:
        word_lst = [word.upper() for word in file.read().split('\n') if len(word) == word_length]

    score = 0
    print(f"{word_length}-Letter Wordle, by Jayden")
    print(f"In this game, you have {max_guesses} chances to guess a {word_length}-letter word.")
    print("After each guess, the output will be (if guess is FIRST, and secret word is FISTS):\n")
    print('FIRST')
    print('|||||')
    print('==/--')
    print(f'{max_guesses} chances left.\n')
    print('The "=" character means a correct letter in the correct position.')
    print('The "-" character means a correct letter in the wrong position.')
    print('The "/" character means a wrong letter that is not in the secret word.')
    print('Alright, now you know the rules, let\'s get started!')

    while True:
        secret_word = random.choice(word_lst)
        guesses = max_guesses
        not_in_word = []  # List to track letters not in the secret word

        while guesses > 0:
            # Display letters not in the secret word
            if not_in_word:
                vowels = sorted([letter for letter in not_in_word if letter in 'AEIOU'])
                consonants = sorted([letter for letter in not_in_word if letter not in 'AEIOU'])
                print(f"Letters not in the word: {', '.join(vowels + consonants)}")

            guess = input(f"\nEnter your {word_length}-letter guess (or type GIVE UP to forfeit the round, or QUIT to quit): ").upper()

            if guess == 'QUIT':
                print(f'\nYour final score is {score}.')
                print('Thanks for playing! Goodbye!')
                return

            if guess == 'GIVE UP':
                print(f'\nYou gave up! The secret word was: {secret_word}')
                print('Moving to the next round...\n')
                break  # End the current round and move to the next one

            if len(guess) != word_length:
                print(f'Invalid guess. Please enter a {word_length}-letter word.')
                continue

            if guess not in word_lst:
                print('Invalid word. Please enter a valid word from the word list.')
                continue

            if guess == secret_word:
                print(f'{guess}\n{"|" * word_length}\n{"=" * word_length}')
                score += 1
                greet = get_greet(guesses)
                print(f'{greet} You guessed the word!')
                if not play_again(score):
                    return
                break

            # Provide feedback
            print(f'{guess}\n{"|" * word_length}')
            feedback = [' '] * word_length
            secret_word_used = [False] * word_length  # Track matched letters in the secret word

            # First pass: Check for correct positions
            for i in range(word_length):
                if guess[i] == secret_word[i]:
                    feedback[i] = '='
                    secret_word_used[i] = True

            # Second pass: Check for correct letters in wrong positions
            for i in range(word_length):
                if feedback[i] == ' ':  # Only process unmatched letters
                    for j in range(word_length):
                        if guess[i] == secret_word[j] and not secret_word_used[j]:
                            feedback[i] = '-'
                            secret_word_used[j] = True
                            break
                    else:
                        feedback[i] = '/'  # Letter is not in the secret word
                        if guess[i] not in not_in_word:
                            not_in_word.append(guess[i])  # Add to not_in_word list

            print(''.join(feedback))

            guesses -= 1
            print(f'\n{guesses} chances left.')

        if guesses == 0:
            print(f'\nYou ran out of guesses! The secret word was {secret_word}.')
            print(f'Your current score is {score}.')
            if not play_again(score):
                return


if __name__ == '__main__':
    main()
