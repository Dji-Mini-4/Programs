def main():
    import random, sys
    try:
        import pyperclip; p_ins = True
    except:
        p_ins = False
        pass
    
    def leet(text: str) -> str:
        'Translates the given text and return the "leetspeak" form.'
        char_map = {
            'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'],
            'e': ['3'], 'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'],
            'k': [']<'], 'o': ['0'], 's': ['$', '5'], 't': ['7', '+'],
            'u': ['|_|'], 'v': ['\\']
        }

        tran_leet = ''
        for char in text:
            if char.lower() in char_map and random.random() <= 0.9:
                char.lower()
                poss_leet = char_map[char.lower()]
                leet_rpl = random.choice(poss_leet)
                tran_leet += leet_rpl
            else:
                tran_leet += char
        
        return tran_leet

    print('\nL3375P34]< (Leetspeak), by Jayden')
    print('This method of speaking online is the coolest way... at least in the 90s.')
    print('\nEnter your message:')
    
    english = input('> '); print()
    leet_speak = leet(english)
    print(leet_speak)

    if p_ins:
        print('\nDo you want to copy your leet speak message? (Y/N)')
        yes_no = input('> '); yes_no = yes_no.lower()
        if yes_no == 'y':
            pyperclip.copy(leet_speak)
            print('(full leetspeak message copied to your clipboard.)')
            sys.exit()
        else:
            print('Thanks!')
            sys.exit()
    else:
        print('Thanks!')
        sys.exit()
    
if __name__ == '__main__':
    main()