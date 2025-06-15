def main():
    try:
        import pyperclip # type: ignore
        pyp_installed = True
    except ImportError:
        pass
        pyp_installed = False

    print('Password Encoder, by Jayden\n')
    print('\nWelcome to the Password Encoder!\n')
    print('It works like this:')
    print('                                                             ')    
    print('A    B    C    D    E    F    G    H    I    J    K    L    M')
    print('1    2    3    4    5    6    7    8    9    10   11   12  13')
    print('')
    print('N    O    P    Q    R    S    T    U    V    W    X    Y    Z')
    print('14   15   16   17   18   19   20   21   22   23   24   25   26')
    print('                                                              ')   
    print('For example, your password is \'hello\' and your secret number is 13:')
    print('First, translate it to numbers: 8 5 12 12 15 (spaces and other characters dosen\'t matter, you need to throw them away, but keep the order of the letters and numbers)')
    print('Then, add the first digit of the secret number to the first number, the second digit of the secret number to the second number, and so on: 8+1 5+3 12+3 12+1 15+3')
    print('After that, translate the numbers back to letters: IHOMO')
    print('So, the encoded password is \'IHOMO\'.\n')
    print('Note: The password is case-insensitive.')
    print('Another note: if your password have numbers, translate them to word form. For example, 1 is one, 2 is two, and so on.')
    print('You can encode your password so that it\'s super secure! (returned in uppercase)')
    print('You can also decode your password if you know the secret number. (returned in uppercase)\n')
    encode_or_decode = input('Would you like to (1)encode or (2)decode a password? ').lower()
    if encode_or_decode == '1' or encode_or_decode == 'encode':
            encoded_password = encode()
            print('\nYour encoded password is:', encoded_password)
            if pyp_installed == True:
                pyperclip.copy(encoded_password)
                print('The encoded password has been copied to your clipboard.')
            else:
                pass
    elif encode_or_decode == '2' or encode_or_decode == 'decode':
            decoded_password = decode()
            print('\nYour decoded password is:', decoded_password)
            if pyp_installed == True:
                pyperclip.copy(decoded_password)
                print('The decoded password has been copied to your clipboard.')
            else:
                pass
        
    def encode():
        password = input('\nEnter a password (only letters are encoded; other characters will be ignored): ')
        pass_num = input('\nEnter the secret number (digits only): ')

        try:
            pass_num = int(pass_num)
        except ValueError:
            print('The number you entered is not valid.')
            pass_num = input('Enter the secret number (digits only): ')
        # Remove non-alphabetic characters from the password
        password = ''.join([char for char in password if char.isalpha()])
        pass_num = [int(digit) for digit in pass_num]  # Convert pass_num to a list of integers

        encoded_password = ''

        for i, char in enumerate(password):
            shift = pass_num[i % len(pass_num)]  # Cycle through pass_num if it's shorter than the password
            if char.islower():  # Handle lowercase letters
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():  # Handle uppercase letters
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encoded_password += new_char  # Append the new character to the encoded password

        encoded_password = encoded_password.strip()  # Remove the trailing space (if any)
        encoded_password = encoded_password.upper()  # Convert the encoded password to uppercase
        return encoded_password

    def decode():
        encoded_password = input('Enter the encoded password (only letters decoded; spaces will be ignored): ')
        pass_num = input('Enter the secret number (digits only): ')

        # Remove spaces from the encoded password and convert to lowercase
        encoded_password = ''.join([char for char in encoded_password if char.isalpha()]).lower()
        pass_num = [int(digit) for digit in pass_num]  # Convert pass_num to a list of integers

        decoded_password = ''

        for i, char in enumerate(encoded_password):
            shift = pass_num[i % len(pass_num)]  # Cycle through pass_num if it's shorter than the password
            new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))  # Decode as lowercase
            decoded_password += new_char

        decoded_password = decoded_password.upper()
        return decoded_password

if __name__ == '__main__':
    main()
