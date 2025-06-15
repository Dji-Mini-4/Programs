from random import uniform; from time import sleep; from time import time

def main():
    while True:
        def check_rules(diff_time):
            if diff_time < 5:
                print('You pressed Enter before "DRAW!" appears, you lose.')
                exit()
            elif diff_time > 30:
                print('You pressed Enter {}ms after "DRAW!" appears. Too slow, you lose.'.format(diff_time))
                exit()
            else:
                print('Your flexibility this time is {}ms. Good job! '.format(diff_time))
                exit()
                    
        print('\nflexibility test, by Jayden')
        print('\nPress Enter when you see "DRAW!". If you dont\'t press Enter in 0.3 seconds or you pressed Enter before "DRAW!" appears, you will lose.')
        input('Press Enter to begin...')
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
        check_rules(diff_time)

if __name__ == '__main__':
    main()