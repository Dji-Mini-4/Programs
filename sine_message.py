def main():
    import math, sys, shutil, time

    WIDTH, _ = shutil.get_terminal_size()
    WIDTH -= 1

    print('Sine message, by Jayden')
    print('(Press Ctrl+C to quit.)\n')
    print(f'What message would you like to display? (Max {WIDTH // 2} chars.)')

    while True:
        message = input('> ')
        if (1 <= len(message) <= (WIDTH // 2)):
            break
        print(f'The message must be 1 to {WIDTH // 2} characters long.')

    step = 0.0
    multiplier = (WIDTH - len(message)) / 2
    try:
        while True:
            sine_step = math.sin(step)
            padding = ' ' * int((sine_step + 1) * multiplier)
            print(padding + message)
            time.sleep(0.06)
            step += 0.25
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()