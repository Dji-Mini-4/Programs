def main():
    import os, pygame, keyboard
    from time import sleep
    
    print('\nSound Player, by Jayden')
    print('This program helps you play a sound file for you if you don\'t have the media player :)\n')
    print('Now, Enter the FULL PATH of your sound file (e.g. "C:\\Users\\Someone\\my_sound.mp3")')
    print('                                     Remember to add ".mp3"                 ^^^^')
    sound_dir = input('> ')
    while not os.path.exists(sound_dir):
        sound_dir = input('\nThat path does NOT exists. Enter the FULL PATH and remember to add ".mp3":\n> ')

    def get_progress():
        current_pg = pygame.mixer.music.get_pos()
        current_pos = current_pg / 1000
        return current_pos
    
    while True:
        loop = input('\nWould you like to loop the sound? (Y/N):\n> '); loop = loop.upper()
        if loop == 'Y' or loop == 'YES':
            loop = True; break
        elif loop == 'N' or loop == 'NO':
            loop = False; break
        else:
            print('That is not valid.', end='')
            continue
    
    if loop:
        while True:
            loop_time = input('Please enter the amount of loops you want to loop or press Enter on the empty line to loop infinite times. DON\'T ENTER 0 OR 1. IT IS NOT VALID.\n> ')
            if loop_time == '':
                loop_time = 'inf'; break
            elif loop_time.isnumeric() and loop_time != '0' and loop_time != '1':
                loop_time = int(loop_time); break
            else:
                print('That is not valid.')
                continue
    
    print('\nPress Enter to start... (Ctrl-C to quit and press P to pause & countinue)'); input()

    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_dir)
    try:
        if loop:
            sound.play(loops=loop_time)
        else:
            sound.play()
    except:
        sound.play(loops=10000000**1000000000000**9999999999999999**999999999999999999**10000000000000000**10384703984701392875042389572340897)
    
    pause = False
    while pygame.mixer.music.get_busy():
        if keyboard.is_pressed('p') and not pause:
            pygame.mixer.pause()
            pause = True
        elif keyboard.is_pressed('p') and pause:
            pygame.mixer.unpause()
            pause = False
        progress = get_progress()
        print('\n' * 100)
        print(f'Current progress (seconds): {progress} / {sound.get_length()}')
        sleep(1)
    
if __name__ == '__main__':
    main()