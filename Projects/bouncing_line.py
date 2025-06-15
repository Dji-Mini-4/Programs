import os, time, sys

def move_cursor_top():
    # ANSI escape code to move cursor to top-left
    print('\033[H', end='')

print('Bouncing Line, by Jayden')
input('Press Enter to start, and Ctrl-C to exit.')

try:
    raw_terminfo = os.get_terminal_size()
    height = raw_terminfo.lines - 2
    width = raw_terminfo.columns - 1
except OSError:
    height = 20
    width = 40

line_char_down = 'v'
line_char_up = '^'

try:
    # Print enough blank lines to fill the screen once, so cursor movement works
    print('\n' * (height + 2))
    while True:
        # Waterfall growing down
        for i in range(1, height + 1):
            move_cursor_top()
            for _ in range(i):
                print(line_char_down * width)
            for _ in range(height - i):
                print()
            sys.stdout.flush()
            time.sleep(0.05)
        # Waterfall shrinking up
        for i in range(height, 0, -1):
            move_cursor_top()
            for _ in range(i):
                print(line_char_up * width)
            for _ in range(height - i):
                print()
            sys.stdout.flush()
            time.sleep(0.05)
except KeyboardInterrupt:
    print('\nExited.')