def main():
    from random import randint; from time import sleep
    print('\n\nLucky Number Giver, by Jayden')
    print('\nHi! We are about to tell you your lucky number between 0 and 100!')
    name = input('\nWhat\'s your name, by the way?\n'); name = name.title()
    print(f'Alright, {name}, ')
    input('Press Enter to reveal...\n')
    number = randint(0, 100)
    print('Your lucky number is...\n')
    sleep(1.5)
    print('<drum roll>\n')
    sleep(2.0)
    print(number, '!', sep='')
    print('\nIf you see your number, you\'re in luck!')
    exit()

if __name__ == '__main__':
    main()