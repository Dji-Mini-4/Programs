
def main():
    import random, os

    raw_width = os.get_terminal_size()
    width = raw_width.columns
    def random_str(ter_width):
        'Return the filling needed for the bomb string.'
        CHAR_LIST = [chr(i) for i in range(33, 127)]
        left_filling = []
        repeat = int((ter_width // 2) / 2)
        right_filling = []
        for i in range(repeat):
            left_filling.append(str(random.choice(CHAR_LIST)))
        for i in range(repeat):
            right_filling.append(str(random.choice(CHAR_LIST)))

        left_filling = ''.join(left_filling)
        right_filling = ''.join(right_filling)
        random_str = left_filling + '__Bombing_Your_Screen__' + right_filling
        return random_str
    
    print('Bomb Your Screen (Waterfall), by Jayden')
    input('\nAre you ready? Press Ctrl + C to stop, press Enter to start...')
    while True:
        try:
            print(random_str(ter_width=width))
        except KeyboardInterrupt:
            print('\n\n')
            break

if __name__ == '__main__':
    main()