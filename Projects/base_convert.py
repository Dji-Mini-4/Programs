def translate(number: int, base: int) -> str:
    'Return the number provided in base n. (letters are in uppercase)'
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    while number:
        translated += digits[number % base]
        number //= base
    return translated[::-1]