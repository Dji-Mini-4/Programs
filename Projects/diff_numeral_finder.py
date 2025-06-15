from time import sleep
from base_convert import translate

print('Number Finder in Different Numeral Systems, by Jayden')
print('This program will help you find the number in different numeral systems (e.g., base-16).')

while True:
    print('\nDo you want to:')
    print('(1) Translate a base-10 number to a specific base (e.g., 255 -> base-16 "ff")')
    print('(2) Translate a number from a specific base to base-10 (e.g., "ff" -> 255)')
    while True:
        mode = input('Enter 1 or 2: ')
        if mode in ('1', '2'):
            break
        print('Invalid input. Enter 1 or 2.')

    print('\nEnter the base of the numeral system (2 ~ 36):')
    while True:
        num_base = input('> ')
        if num_base.isdecimal() and 2 <= int(num_base) <= 36:
            num_base = int(num_base)
            break
        print('That\'s not a valid base. Please enter a number between 2 and 36.')

    if mode == '1':
        print('\nEnter the base-10 number you want to translate:')
        while True:
            raw_decnum = input('> ')
            if raw_decnum.isdecimal():
                raw_decnum = int(raw_decnum)
                break
            print('That is not a valid base-10 number.')

        print('\nYour TRANSLATED number is...')
        sleep(1.2)
        print('< drum roll >')
        sleep(1.2)

        result = translate(raw_decnum, num_base)
        result = result.center(len(result) + 12)
        result_len = len(result)
        print('=' * result_len)
        print(result)
        print('=' * result_len)
        print()

    elif mode == '2':
        print('\nEnter the translated text of the number:')
        while True:
            raw_encnum = input('> ')
            try:
                result = str(int(raw_encnum, num_base))
                break
            except ValueError:
                print('The input is not valid for the specified base. Please try again.')

        print('\nYour TRANSLATED number is...')
        sleep(1.2)
        print('< drum roll >')
        sleep(1.2)

        result = result.center(len(result) + 12)
        result_len = len(result)
        print('=' * result_len)
        print(result)
        print('=' * result_len)
        print()

    while True:
        pe = input('Press Enter to do it again... (or type QUIT to quit): ')
        if pe.upper() == 'QUIT':
            print('Goodbye!')
            quit()
        elif pe == '':
            break
        else:
            print('Invalid.')
            continue