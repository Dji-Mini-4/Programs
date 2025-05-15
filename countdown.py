def main():
    import time, sys
    from sevseg import translate
    
    print('Countdown, by Jayden\n')
    while True:
        num_second = input('Enter the seconds to count:\n> ')
        if not num_second.isnumeric():
            print('That is not valid.')
            continue
        else:
            break
    num_second = int(num_second)
    
    rawhours = int(num_second // 3600)
    rawminutes = int((num_second % 3600) // 60)

    if (1 <= rawhours <= 2):
        print('Okay, more than ONE hour miiiight be long... Do you REALLY want to wait? Yes? OK...')
    elif rawhours < 2:
        print('Now you are just PURE SILLY... I mean, REALLY!!?\nI\'ve never seen a person trying to use this program to count HOURS OF TIME...')
    elif rawminutes == 3:
        print('Trying to eat a pack of instant noodles? Hope you poured boiled water BEFORE you start the timer...')
    elif (3 < rawminutes <= 8):
        print('Really waiting that long? I can accept if you are doing some sort of science experiment...')

    input('\n(Press Ctrl-C to quit at anytime.)\nPress Enter to continue...')
    try:
        while True:
            print('\n' * 100)

            hours = str(num_second // 3600)
            minutes = str((num_second % 3600) // 60)
            seconds = str(num_second % 60)

            hour_str = translate(hours, 2)
            hour_t, hour_m, hour_d = hour_str.splitlines()

            minutes_str = translate(minutes, 2)
            min_t, min_m, min_d = minutes_str.splitlines()

            seconds_str = translate(seconds, 2)
            sec_t, sec_m, sec_d = seconds_str.splitlines()

            print(hour_t + '     ' + min_t + '     ' + sec_t)
            print(hour_m + '  *  ' + min_m + '  *  ' + sec_m)
            print(hour_d + '  *  ' + min_d + '  *  ' + sec_d)
            print('\n' * 5)

            if not num_second:
                print('\n' * 100)
                print(hour_t + '     ' + min_t + '     ' + sec_t)
                print(hour_m + '  *  ' + min_m + '  *  ' + sec_m)
                print(hour_d + '  *  ' + min_d + '  *  ' + sec_d)
                print('\n' * 5)
                time.sleep(1)
                print('    * * * TIME OUT * * *')
                print()
                break

            time.sleep(1)
            num_second -= 1
    except KeyboardInterrupt:
        print('\n\n\n'); sys.exit()

if __name__ == '__main__':
    main()
