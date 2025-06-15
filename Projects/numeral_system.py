def main():
    print('\nNumeral Systems, by Jayden')
    print('We are used to count in Decimal System (10-based), but there are many other ones out there.')
    print('The common ones are:\nDecimal (10-based, which is the base we are used to)\nHex (16-based, including "A", "B", "C", "D", "E", "F") and\nBinary (2-based with ONLY 0 and 1.)')
    print('\nIn this program, you will see a number in 3 different forms (DEC, HEX and BIN).\n')
    
    while True:
        number = input('Enter the highest number (the program will print out 1 ~ your number):\n> ')
        if not number.isnumeric():
            print('That is not valid.')
            continue
        elif int(number) > 40:
            print('That is a lot. But don\'t worry, it is fine. (In the Python Shell, it may squeeze it btw)')
            break
        break

    number = int(number)
    input('\nPress Enter to start...')

    print()
    for d in range(number):
        d += 1
        h = hex(d)[2:].upper()
        b = bin(d)[2:]
        print(f'DEC: {d}      HEX: {h}      BIN: {b}')
if __name__ == '__main__':
    main()