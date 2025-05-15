def print_demo():
    print('\nSeven-Segment Display Module, by Jayden')
    print('This program is meant to be run as a module.')
    print('Now you are running this program directly, I will print out a demo for you.')
    print()
    print('A seven-segment display has (obvieously) seven parts as labled 1-7 in the following:')
    print(''' 
  __1__
 |     |
 2     3
 |__4__|
 |     |
 5     6
 |__7__|
          
using this, we can make digits 0-9:
 __        __     __             __     __     __     __     __    
|  |  |    __|    __|    |__|   |__    |__       |   |__|   |__|
|__|  |   |__     __|       |    __|   |__|      |   |__|    __|
              
''')
    print('You can import the get_sevseg_str function using the following example code:\n')
    print('    import sevseg')
    print('    number = sevseg.get_sevseg_str(42, 3)')
    print('    print(number)')
    print('    # will print 42, zero-padded to 3 digits:')
    print('''
     __        __
    |  | |__|  __|     
    |__|    | |__
          
''')
    return

def translate(original_number, min_length=0):
    'Return a seven-segment string.'
    original_number = str(original_number).zfill(min_length)
    rows = ['', '', '']

    for i, number in enumerate(original_number):
        if number == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
        elif number == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif number == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif number == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif number == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif number == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif number == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif number == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif number == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif number == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif number == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        if i != len(original_number) - 1 and original_number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

if __name__ == '__main__':
    print_demo()
