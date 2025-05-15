def main():
    import random, sys

    print('\nPowerball Lottery Simulation Program, by Jayden')
    print('This program let\'s you enjoy the thrill of playing without losing any real money.')
    print('The jackpot is 1.586 million! But the odds are 1 in 292,201,338, so you won\'t win.')
    print('Press Enter to start...'); input()

    while True:
        print('\nEnter the first 5 numbers between 1 and 69, seperate with spaces (e.g. 45 2 8 34 18):')
        player_num = input('> ').split()
        if len(player_num) != 5:
            print('Please enter 5 numbers, seperated by spaces. (e.g. 5 23 9 60 17)')
            continue

        try:
            for i in range(5):
                player_num[i] = int(player_num[i])
        except ValueError:
            print('Please enter NUMBERS for your input. (e.g. 5 23 9 60 17)')
            continue

        for i in range(5):
                if not (1 <= player_num[i] <= 69):
                    print('The 5 numbers MUST be between 1 and 69. (e.g. 5 23 9 60 17)')
                    continue
            
        if len(set(player_num)) != 5:
            print('You cannot enter 5 REPEATING numbers.')
            continue

        break

    while True:
        print('\nEnter the POWERBALL number between 1 and 26: (e.g. 18)')
        powerball = input('> ')

        try:
            powerball = int(powerball)
        except ValueError:
            print('Your powerball MUST be a number. (e.g. 18)')
            continue

        if not (1 <= powerball <= 26):
            print('Your powerball number is out of the range (1-26). Enter something like this: 18')
            continue

        break

    while True:
        print('\nHow many times shall I generate? (max 1000000)')
        num_sim = input('> ')

        try:
            num_sim = int(num_sim)
        except:
            print('Your input MUST be a number. (e.g. 1000)')
            continue

        if not (1 <= num_sim <= 1000000):
            print('You can only play 1 to 1000000 times.')
            continue

        break

    waste = 0
    print(f'The cost is ${2 * num_sim} to play {num_sim} times. But don\'t worry, you\'ll win it all back.')
    input('Press Enter to start...\n')

    poss_nums = list(range(1, 70))
    for i in range(num_sim):
        random.shuffle(poss_nums)
        win_num = poss_nums[0:5]
        win_pwb = random.randint(1, 26)

        all_winning = f'The winning numbers are: {win_num[0]} {win_num[1]} {win_num[2]} {win_num[3]} {win_num[4]} and {win_pwb}'
        all_winning = all_winning + ' ' * (50 - len(all_winning))
        print(f'{all_winning}', end='')
        if (set(player_num) == set(win_num) and powerball == win_pwb):
            print('\nYOU WON THE JACKPOT !!!!!!!')
            print('You\'ll be a BILLIONARE if this was real!')
            break
        else:
            print(' You have lost.')
            waste += 2
    
    print(f'You have wasted ${waste}')
    print('Thanks for playing!')
    sys.exit()

if __name__ == '__main__':
    main()