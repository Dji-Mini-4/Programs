def main():
    import time, random

    print('\nNinety-Nine bottles, by Jayden')
    bottles = 99

    while True:
        pause = input('\nInput the time to pause every time or enter RANDOM to randomly generate pause amaount between 2s and 3s (enter 0 if you want to see the whole song at once):\n> '); pause = pause.upper()
        if pause == 'RANDOM' or pause == 'R':
            pause = random.randint(2, 3); break
        
        try:
            pause = int(pause)
        except:
            try:
                pause = float(pause)
            except:
                print('That is not valid.')
                continue
        break

    print('Press Enter to start, and Ctrl-C to stop...'); input()
    
    try:
        while bottles > 1:
            print(f'{bottles} bottles of milk on the wall,'); time.sleep(pause)
            print(f'{bottles} bottles of milk,'); time.sleep(pause)
            print('Take on down, pass it around,'); time.sleep(pause); bottles -= 1
            if bottles == 1:
                print(f'{bottles} bottle of milk on the wall!\n'); time.sleep(pause)
            else:
                print(f'{bottles} bottles of milk on the wall!\n'); time.sleep(pause)
        
        print('1 bottle of milk on the wall,'); time.sleep(pause)
        print('1 bottle of milk,'); time.sleep(pause)
        print('Take one down, pass it around,'); time.sleep(pause)
        print('No more bottles of milk on the wall!')
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()