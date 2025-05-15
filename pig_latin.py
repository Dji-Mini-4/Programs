def main():
    try:
        import pyperclip
    except ImportError:
        pass

    print('Pig Latin, by Jayden')
    print('In this program, it takes an input from the user, then translate it to pig latin.')
    print('It works like this:')
    print('If the word begins with a constant (every letter other than a, e, i, o, u), it moves the first letter to the end, then add "ay" to it.\n"latin" -> "atinlay", "height" -> "eighthay"\n')
    print('Or if the word begins with a vowel (a, e, i, o, u), it simply adds "yay" on the end.\n"umbrella" -> "umbrellayay", "international" -> "internationalyay"')
    print('Alright, let\'s start!\n')
    while True:
        original = input('Enter the message you want to translate:\n> '); original = original.split()
        error = False
        for s in original:
            if len(s) == 0:
                print('That is not valid.')
                error = True
                break
        if not error:
            break
        

    latins = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in original:
        first_letter = i[0]
        if first_letter not in vowels:
            temp_latin = f'{i[1:]}{first_letter}ay'
        else:
            temp_latin = f'{i}yay'
        latins.append(temp_latin)
    
    latin = ' '.join(latins)
    print(f'\nYour translated message is:\n{latin}')
    try:
        pyperclip.copy(latin)
        print('(Full translate Pig Latin copied to your clipboard.)')
        exit()
    except:
        pass

if __name__ == '__main__':
    main()
