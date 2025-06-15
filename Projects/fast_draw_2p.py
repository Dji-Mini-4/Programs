def main():
    from random import uniform; from time import sleep; from time import time # import the function we need
    isitp1 = True
    def first_version_fast_draw(isitp1):
        player1 = input('\nPlayer one, enter your name: '); player1 = player1.capitalize()
        player2 = input('Player two, enter your name: '); player2 = player2.capitalize()
        print('\nHere\'s the rules: \nPress Enter when you see "DRAW!". If you dont\'t press Enter in 0.3 seconds or you pressed Enter before "DRAW!" appears, you will lose.')            
        print('\nAlright, now you know the rules, you two will meet on the battleground to see who can press Enter 0.3s after "DRAW!" appears!\nPress Enter to begin...')
        while True:
            def check_rules(diff_time: float|int, isitp1: bool, player1: str, player2: str):
                'Checks the rules and exit the game. (executed after diff_time is defined and adjusted.)'
                if isitp1 == True:
                    name = player1; cname = player2
                else:
                    name = player2; cname = player1

                if diff_time < 5:
                    print(f'{name}, you pressed Enter before "DRAW!" appears, you lose.')
                    print(f'\nCongrats, {cname}, you successfully survived on the battlefield! You win!')
                    exit()
                elif diff_time > 30:
                    print(f'{name}, you pressed Enter {diff_time}ms after "DRAW!" appears. Too slow, you lose.')
                    print(f'\nCongrats, {cname}, you successfully survived on the battlefield! You win!')
                    exit()
                else:
                    print(f'Your flexibility this time is {diff_time}ms. You win! Good job!')
                    print(f'\nSorry, {cname}, looks like that {name} achieved the goal before you. Bad luck!')
                    exit()
            
            sleep(uniform(0, 0.3))
            print('\nIt is high noon...')
            sleep(uniform(2, 4.3))
            print('\nDRAW!')
            start_time = time()
            timer_input = input(); del timer_input
            end_time = time()
            raw_diff_time = end_time - start_time
            diff_time = raw_diff_time * 100
            diff_time = round(diff_time, 1)
            if isitp1 == True:
                check_rules(diff_time, isitp1, player1, player2)
            elif isitp1 == False:
                check_rules(diff_time, isitp1, player1, player2)

            if isitp1 == True:
                isitp1 = False
            else:
                isitp1 = True
    
    def second_version_fast_draw(isitp1):
        score = {'p1': 0, 'p2': 0}
        player1 = input('\nPlayer one, enter your name: '); player1 = player1.capitalize()
        player2 = input('Player two, enter your name: '); player2 = player2.capitalize()
        print('\nHere\'s the rules: \nPress Enter when you see "DRAW!". If you dont\'t press Enter in 0.3 seconds or you pressed Enter before "DRAW!" appears, you will lose.')
        print('\nAlright, now you know the rules, you two will meet on the battleground to see who can press Enter 0.3s after "DRAW!" appears!\nPress Enter to begin...')
        
        while True:
            def check_rules_after(p1d: float|int, p2d: float|int, isitp1: bool, player1: str, player2: str):
                p1, p2 = player1, player2
                if p1d < 5:
                    print(f'{p1}, you pressed Enter before "DRAW!" appears, you lose.')
                    print(f'\nCongrats, {p2}, you successfully survived on the battlefield! You win!')
                    score['p2'] += 1
                elif p2d < 5:
                    print(f'{p2}, you pressed Enter before "DRAW!" appears, you lose.')
                    print(f'\nCongrats, {p1}, you successfully survived on the battlefield! You win!')
                    score['p1'] += 1
                elif p1d > p2d:
                    print(f'Congrats, {p1}, you survived using your {p1d}ms react time! You win!')
                    score['p1'] += 1
            
            input('')
            sleep(uniform(0, 0.3))
            print('\nIt is high noon...')
            sleep(uniform(2, 4.3))
            print('\nDRAW!')
            start_time = time()
            timer_input = input(); del timer_input
            end_time = time()
            raw_diff_time = end_time - start_time
            diff_time = raw_diff_time * 100
            diff_time = round(diff_time, 1)
            if isitp1 == True:
                p1_diff_time = diff_time
                print(f'{player1}, your react time is {p1_diff_time}! Now it\'s {player2}\'s turn, press Enter to continue...'); input()
            else:
                p2_diff_time = diff_time
                check_rules_after(p1_diff_time, p2_diff_time, isitp1, player1, player2)

            if isitp1 == True:
                isitp1 = False
            else:
                isitp1 = True

    print('\nflexibility test, by Jayden')
    print('\nWhat version of fast draw would you like to play?')
    print('The first version\'s goal is to be the first one who can press Enter 0.3s after "DRAW!" appears.\nThe second one has multiple rounds and in each round you compete against each other and try to press Enter as fast as you can after "DRAW!" appears.')
    print('Now, are you ready to choose?', end='')
    version = input('Enter 1 for the 1st version. Enter 2 for the 2nd version.')
    while version != '1' and version != '2':
        print('That is not a valid choice. Enter 1 for the 1st version, enter 2 for the 2nd version. ')
        version = input('Enter 1 for the 1st version. Enter 2 for the 2nd version.')
    if version == '1':
        first_version_fast_draw(isitp1)
    else:
        second_version_fast_draw(isitp1)

if __name__ == '__main__':
    main()
