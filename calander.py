import datetime, os

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')
month_dict = {1: MONTHS[0], 2: MONTHS[1], 3: MONTHS[2], 4: MONTHS[3], 5: MONTHS[4], 6: MONTHS[5], 
              7: MONTHS[6], 8: MONTHS[7], 9: MONTHS[8], 10: MONTHS[9], 11: MONTHS[10], 12: MONTHS[11]}

print('Calendar Maker, by Jayden')

while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')


def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):  # (!) Try changing the 4 to a 5 or 10.
            calText += blankRow

        # Check if we're done with the month:
        if currentDate.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

text_month = month_dict[month]
save_file = input(f'Would you like to save the calander of {text_month}, {year} into a text file called "calander_{year}_{month}.txt"? (Y/N)\n> ')
save_file = save_file.upper()
if save_file.startswith('Y'):
    print('Please identify the path. (e.g. "C:\\Users\\YourName\\Programs", and NO NAME (no "calender_XX_XX.txt" at the end), just the folder path)')
    while True:
        file_path = input('> ')
        if not os.path.isdir(file_path):
            print('That is not valid.')
            continue
        break
    filename = 'calander_{}_{}.txt'.format(year, month)
    with open(filename, 'w') as file_obj:
        file_obj.write(calText)
    print('Thanks!')
    exit()
else:
    print('Thanks!')
    exit()