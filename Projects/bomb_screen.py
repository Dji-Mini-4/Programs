def main():
    import random, os

    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # Default width if not in a real terminal

    def random_str(ter_width):
        'Return the filling needed for the bomb string.'
        CHAR_LIST = [chr(i) for i in range(33, 127)]
        bomb_text = '__Bombing_Your_Screen__'
        fill_len = max(0, (ter_width - len(bomb_text)) // 2)
        left_filling = ''.join(random.choice(CHAR_LIST) for _ in range(fill_len))
        right_filling = ''.join(random.choice(CHAR_LIST) for _ in range(fill_len))
        return left_filling + bomb_text + right_filling

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