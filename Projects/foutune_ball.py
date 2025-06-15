def main():
    import time
    import random

    def slow_print(text: str, sleep_time: int | float = 0.15):
        'Slowly display the text with spaces in each character and lowercase the "i"s (other are all uppercase)'
        text = text.upper()
        for char in text:
            if char == 'I':
                print('i ', end='', flush=True)
            else:
                print(char + ' ', end='', flush=True)
            time.sleep(sleep_time)
        print('\n\n')
    
    print()
    slow_print('Magic Fortune Ball, by Jayden')
    time.sleep(0.2)

    while True:
        slow_print('Ask me your yes/no question.')
        input('> ')

        replies = [
            'let me think about this...' ,
            'Do you really want to know..?' ,
            'You don\'t want to hear this...' ,
            'Hmm...pretty interesting...' ,
            'do you sure you want to know..?' ,
            'and what will you do when you have the answer? let\'s see..' ,
            'you may not like the answer...'
        ]

        print('\n\n')
        slow_print(replies[random.randint(0, len(replies) - 1)])
        slow_print('.' * random.randint(7, 10), random.uniform(0.5, 0.8))

        slow_print('I have the answer...', 0.2)
        time.sleep(0.8)

        answers = [
            'affirmative' ,
            'maybe... you figure it yourself' ,
            'it\'s yes' ,
            'sorry, but no' ,
            'sometimes you will like it, but no' ,
            'yes, but you may not be happy about it' ,
            'true' ,
            'false' ,
            'surely' ,
            'a big \'no\'' ,
            'I doubt it...' ,
            'certain' ,
        ]

        slow_print(random.choice(answers), 0.05)
        print('\n\n')
        time.sleep(1.5)
        slow_print('do you like to do it again? Y/N', 0.09)
        while True:
            yorn = input('> ').upper()
            if yorn in ['Y', 'N']:
                break
            slow_print('That is invalid.')
        
        if yorn == 'Y':
            continue
        elif yorn == 'N':
            quit()

if __name__ == '__main__':
    main()