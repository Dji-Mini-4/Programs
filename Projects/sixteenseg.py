def get_sixtseg_str(text: str) -> str:
    '''
Return a sixteen-segment string.

Only accept alphabet or numbers, else will raise ValueError for invalid characters.

Remember to add a try/else statement to handle errors.
'''

    text = str(text)
    result = ['', '', '', '', '', '', '', '', '']
    poss_chars = []
    for i in range(48, 58):
        poss_chars.append(chr(i))
    for i in range(65, 91):
        poss_chars.append(chr(i))
    for i in range(97, 123):
        poss_chars.append(chr(i))

    for char in text:
        if char not in poss_chars:
            raise ValueError('Invalid character for translating (only accept alphabet & numbers)')