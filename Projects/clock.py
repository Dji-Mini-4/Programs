def main():
    import sys, time
    from sevseg import translate

    print('\nDigital Clock, by Jayden\nPress Ctrl-C to quit.')
    print('\nPress Enter to start...'); input()

    try:
        while True:
            print('\n' * 100)

            current_time = time.localtime()
            hours = str(current_time.tm_hour % 12)
            minutes = str(current_time.tm_min)
            seconds = str(current_time.tm_sec)
            if hours == '0':
                hours = '12'
            
            hour_str = translate(hours, 2)
            hour_t, hour_m, hour_d = hour_str.splitlines()
            minute_str = translate(minutes, 2)
            min_t, min_m, min_d = minute_str.splitlines()
            sec_str = translate(seconds, 2)
            sec_t, sec_m, sec_d = sec_str.splitlines()

            print(hour_t + '     ' + min_t + '     ' + sec_t)
            print(hour_m + '  *  ' + min_m + '  *  ' + sec_m)
            print(hour_d + '  *  ' + min_d + '  *  ' + sec_d)
            print('\n' * 5)

            while True:
                time.sleep(0.01)
                if time.localtime().tm_sec != current_time.tm_sec:
                    break
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()