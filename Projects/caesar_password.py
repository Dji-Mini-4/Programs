def main():
    try:
        import pyperclip
        pyp_installed = True
    except ImportError:
        pyp_installed = False

    print('\nWelcome to Caesar Password Encode, Decode, and Hacker, also known as the Caesar Cipher!')
    print('This program can encode or decode your password using the Caesar Cipher method.')
    print('For example, if you enter "hello" and the shift value is 3, the encoded password will be "KHOOR".')
    print('Note: The Caesar Cipher method only works for alphabetic characters.')
    print('If you know the shift value, you can decode the password using the same shift value.')
    print('The shift value must be an integer between 1 and 25.')
    print('You can also choose to hack the password by trying all possible shift values.')
    print('Tip for encoding: If your password has numbers inside, enter the word form. (e.g., "123" -> "ONE TWO THREE")')
    print('Let\'s get started!')

    def encode():
        keep_spaces = input('\nDo you want to keep spaces? (y/n): ').strip().lower() == 'y'
        password = input('Enter your password to encode: ').upper()
        while True:
            try:
                shift = int(input('Enter the shift value (1-25): '))
                if 1 <= shift <= 25:
                    break
                else:
                    print('Shift must be between 1 and 25.')
            except ValueError:
                print('Please enter a valid integer.')
        encoded_password = ''
        for char in password:
            if char.isalpha():
                char_code = ord(char) + shift
                if char_code > ord('Z'):
                    char_code -= 26
                encoded_password += chr(char_code)
            elif keep_spaces and char == ' ':
                encoded_password += char
        encoded_password = encoded_password.upper()
        if pyp_installed:
            pyperclip.copy(encoded_password)
            print(f'\nThe encoded password is: {encoded_password}')
            print('The encoded password has been copied to your clipboard.')
        else:
            print(f'\nThe encoded password is: {encoded_password}')
        return

    def decode():
        keep_spaces = input('\nDo you want to keep spaces? (y/n): ').strip().lower() == 'y'
        password = input('Enter your password to decode: ').upper()
        while True:
            try:
                shift = int(input('Enter the shift value (1-25): '))
                if 1 <= shift <= 25:
                    break
                else:
                    print('Shift must be between 1 and 25.')
            except ValueError:
                print('Please enter a valid integer.')
        decoded_password = ''
        for char in password:
            if char.isalpha():
                char_code = ord(char) - shift
                if char_code < ord('A'):
                    char_code += 26
                decoded_password += chr(char_code)
            elif keep_spaces and char == ' ':
                decoded_password += char
        decoded_password = decoded_password.upper()
        if pyp_installed:
            pyperclip.copy(decoded_password)
            print(f'\nThe decoded password is: {decoded_password}')
            print('The decoded password has been copied to your clipboard.')
        else:
            print(f'\nThe decoded password is: {decoded_password}')
        return

    def hack():
        import os
        password = input('\nEnter the password to hack (letters and spaces only): ').upper()
        save_file = input('Do you want to save the hacked passwords to a file? (yes/no): ').strip().lower()
        file_name = ''
        if save_file == 'yes':
            while True:
                file_name = input('Enter the file name (e.g., hacked_passwords.txt): ').strip()
                if not os.path.exists(file_name):
                    break
                print('The file already exists. Enter a different file name.')
        hacked_passwords = []
        for shift in range(1, 26):
            hacked_password = ''
            for char in password:
                if char.isalpha():
                    char_code = ord(char) - shift
                    if char_code < ord('A'):
                        char_code += 26
                    hacked_password += chr(char_code)
                else:
                    hacked_password += char
            hacked_passwords.append(hacked_password.upper())
        if save_file == 'yes':
            with open(file_name, 'w') as write_file:
                for hacked_password in hacked_passwords:
                    write_file.write(f'{hacked_password}\n')
            print(f'\nAll 25 possible passwords have been saved to {file_name}.')
        for i in range(25):
            print(f'code #{i + 1}: {hacked_passwords[i]}')
        return

    print('\nChoose an option:')
    print('1. Encode a password')
    print('2. Decode a password')
    print('3. Hack a password')
    print('4. Exit')
    while True:
        try:
            choice = int(input('Enter your choice (1-4): '))
            if 1 <= choice <= 4:
                break
            else:
                print('Invalid input. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')
    if choice == 1:
        encode()
    elif choice == 2:
        decode()
    elif choice == 3:
        hack()
    else:
        print('Goodbye!')
        return

if __name__ == '__main__':
    main()
