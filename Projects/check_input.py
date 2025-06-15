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
        try:
            value = int(original)
        except ValueError:
            return 'not int'
        if num_range:
            parts = num_range.split()
            if len(parts) != 2:
                return 'invalid range'
            down, up = parts
            if down == 'any':
                down_val = float('-inf')
            else:
                try:
                    down_val = int(down)
                except ValueError:
                    return 'invalid range'
            if up == 'any':
                up_val = float('inf')
            else:
                try:
                    up_val = int(up)
                except ValueError:
                    return 'invalid range'
            if down_val < value < up_val:
                return 'in range'
            elif value < down_val:
                return 'below range'
            elif value > up_val:
                return 'above range'
            elif value == down_val or value == up_val:
                return 'on bound'
        else:
            return 'no range'
    elif check_mode == 'int':
        try:
            int(original)
            return 'int'
        except ValueError:
            return 'not int'
    elif check_mode == 'float':
        try:
            float(original)
            return 'float'
        except ValueError:
            return 'not float'
    elif check_mode == 'check string':
        return original == expect
    else:
        return 'invalid mode'

if __name__ == '__main__':
    print_demo()