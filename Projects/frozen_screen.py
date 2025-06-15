def main():
    print('Frozen Text, by Jayden')
    text = input('Enter the text you want to freeze: ')
    print('Press Ctrl + C to stop, press Enter to start...'); input()
    while True:
        try:
            print(f'{text}{' ' * 5}{text}{' ' * 5}{text}')
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    main()