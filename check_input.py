def print_demo():
    import time
    print('Check-Input Module, by Jayden'); time.sleep(1.5)
    print('This program is meant to be imported rather than run.'); time.sleep(1.5)
    print('But, what this program does, is that it can help you check the input quickly.'); time.sleep(1.5)
    print('For example, checking a input to see if it\'s an integer, and it will return True or False.'); time.sleep(1.5)
    print('Alright, now you know what it can do, I\'m exiting...'); time.sleep(3)
    exit()

def check_input(original, check_mode: str, num_range='', expect = ''):
    original = str(original)
    check_mode = check_mode.lower()
    if check_mode == 'int range':
        if original.isnumeric():
            if num_range:
                up = num_range.split()[1]
                down = num_range.split()[0]
                if up == 'any':
                    up = float('inf')
                elif down == 'any':
                    down = float('-inf')
                if num_range > down and num_range < up:
                    return 'range'
                elif num_range < down:
                    return 'down'
                elif num_range > up:
                    return 'up'
        else:
            return 'not int'
    elif check_mode == 'int':
        if original.isnumeric():
            return 'int'
        else:
            return 'not int'
    elif check_mode == 'float':
        try:
            float(original)
            return 'float'
        except:
            return 'not float'
    if check_mode == 'check string':
        if original == expect:
            return True
        else:
            return False

if __name__ == '__main__':
    print_demo()