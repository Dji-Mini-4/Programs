import random, shutil, time

try:
    import pyperclip
    available = True
except ImportError:
    available = False

def ranstr(len_str: int) -> str:
    'Returns a random string made out of random characters.'
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890`~!@#$%^&*()-_=+]}[{\|;:\'",<.>/?'
    return ''.join(random.choice(chars) for _ in range(len_str))

def copy(text: str, available: bool = False) -> None:
    if available:
        yon = input('Copy? (enter QUIT to quit, enter Y if yes, press Enter for no): ').strip().upper()
        if yon == 'Y':
            print('\n< Copying... >'); time.sleep(0.5)
            pyperclip.copy(text)
            print('\n<    Done    >'); time.sleep(0.2)
        elif yon == 'QUIT':
            print('Goodbye!')
            quit()
        # If Enter or anything else, do nothing

# Get terminal width, ensure minimum width
scr_width = max(4, (shutil.get_terminal_size().columns - 1) // 2)

print('\nTime Waster, by Jayden')
print('This program lets you see a randomly generated string every time you press Enter.')
print('You may find something interesting in there...')

if not available:
    print('(pyperclip not installed, copy-to-clipboard will not be available.)')

print(f'Now, enter the length of the string...or enter RANDOM for a random number... (range: Min 4, Max {scr_width})')
while True:
    width = input('> ').strip().upper()
    if width == 'RANDOM':
        width = random.randint(4, scr_width)
        print(f'The length is {width}.')
        break
    elif width.isdecimal():
        width_int = int(width)
        if 4 <= width_int <= scr_width:
            width = width_int
            break
    print(f"That's not valid. Min 4, Max {scr_width}.")

print('You can enter "Y" when a random string is printed out, and the computer will copy it for you (if you have the pyperclip module installed)')
while True:
    ready = input('Ready? Press Enter to see the first one... (enter QUIT to quit.) ').strip().upper()
    if ready == 'QUIT':
        print('Goodbye!')
        quit()
    elif ready == '':
        break
    else:
        print('Invalid. Enter QUIT or just press Enter.')

while True:
    product = ranstr(width)
    print(f'\n{product}\n')
    copy(product, available)