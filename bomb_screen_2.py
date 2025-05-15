def main():
    from random import choice
    print('\nBomb Screen 2nd Version (Waterfall 2nd Version), by Jayden\n')
    def random_str():
        'return a random string.'
        CHAR_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                     '!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '~', '-', ';', '>', '<', '?', '/', '{', '}', '|', '_']
        filling = []
        for i in range(90):
            filling.append(choice(CHAR_LIST))
        filling = ''.join(filling)
        return filling
    while True:
        try:
            print(random_str())
        except KeyboardInterrupt:
            print('\n\n')
            break

if __name__ == '__main__':
    main()

