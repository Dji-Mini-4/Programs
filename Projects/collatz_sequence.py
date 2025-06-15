def main():
    'Collatz Sequence Program.'
    
    print('\nCollatz Sequence, also known as the 3*n+1 problem, by Jayden')
    print('The rules are simple:')
    print('1. give a starting number')
    print('2. If the number is ODD, then the new number is 3 * number + 1')
    print('3. If the number is EVEN, then the new number is number / 2')
    print('4. If the number is 1, stop.')
    print('\nAlthough it\'s not mathematically proved, it ALWAYS ends at number 1.')
    print('Let\'s start!')
    print('Enter the starting number (or 0 to quit):', end='')
    while True:
        num = input('\n> ')
        if not num.isdecimal(): 
            print('\nThat is invalid.')
            continue
        elif int(num) == 0:
            return
        num = int(num)
        print(f'\n{num}, ', end='')
        while True:
            if num % 2 == 0:
                num = int(num / 2)
            elif num % 2 == 1 and num != 1:
                num = (num * 3) + 1
            elif num == 1:
                pass
            if num != 1:
                print(f'{num}, ', end='')
            else:
                print(num, '\n', end='', sep='')
                break
            

if __name__ == '__main__':
    main()