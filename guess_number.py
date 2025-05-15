def main():
    import random

    def ask_guess() -> int:
        while True:
            test_num = input('> ')
            if test_num.isdecimal():
                if (1 <= int(test_num) <= 100):
                    return int(test_num)
            print('That is invalid. Please enter a number between 1 and 100.')
    
    print('\nGuess the Number, by Jayden')
    secret_num = random.randint(1, 100)
    print('I am thinking a number between 1 and 100 and you have 10 guesses.')
    for i in range(10):
        print(f'You have {10 - i} guesses left. Take a guess.')

        guess = ask_guess()
        if guess == secret_num:
            break

        if guess < secret_num:
            print('That is too low.')
        elif guess > secret_num:
            print('That is too high.')
    
    if guess == secret_num:
        print('You guessed my number!')
    else:
        print(f'Uh-oh! You\'ve ran out of guesses! The secret number I\'m thinking of is: {secret_num}')
    
    print('Thanks for playing!')
    exit()

if __name__ == '__main__':
    main()