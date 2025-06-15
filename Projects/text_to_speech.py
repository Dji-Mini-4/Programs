def main():
    import sys
    try:
        import pyttsx3
    except ImportError:
        print('This program needs the "pyttsx3" module, which you didn\'t have.')
        print('Try install it and then run the program.')
        sys.exit()
    
    tts = pyttsx3.init()

    print('Text To Speech Talker, by Jayden')
    print('Text-to-speech using the pyttsx3 module, which is using:')
    print('1. NSSpeechSynthesizer (on macOS)')
    print('2. SAPI5 (on Windows)')
    print('3. eSpeak (on Linux)')
    print('speech engines.\n')
    print('Enter the text you want the computer to read out loud, or press Enter on the empty line to quit.')

    while True:
        text = input('> ')
        if text == '':
            print('Thanks!')
            sys.exit()
        
        tts.say(text)
        tts.runAndWait()

if __name__ == '__main__':
    main()