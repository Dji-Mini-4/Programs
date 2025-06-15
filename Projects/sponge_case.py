def main():
    import random
    try:
        import pyperclip
    except ImportError:
        pass

    def spongecase(text: str) -> str:
        'Translate the given text to spongecase.'
        sponge = ''
        keep_upper = False
        for char in text:
            if not char.isalpha():
                sponge += char
                continue

            if keep_upper:
                sponge += char.upper()
            else:
                sponge += char.lower()
            
            if random.randint(0, 100) <= 90:
                keep_upper = not keep_upper
        
        return sponge

    print('sPoNgEcAsE, bY jAyDeN\n')
    text = input('eNtEr YoUr MeSsAgE:\n> ')
    sponge_text = spongecase(text)
    print(f'\nyOuR sPoNgEcAsE iS:\n\n{sponge_text}')
    try:
        pyperclip.copy(sponge_text)
        print('\n(fUlL sPoNgEtExt CopIeD To YoUr ClIpBoarD.)')
    except:
        pass

if __name__ == '__main__':
    main()