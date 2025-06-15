def main():
    import random, sys

    print('\nDice roller, by Jayden')
    print('Games like "Dungeon & Dragons" uses special dies such as 4-sided, 8-sided, and even 20-sided ones.')
    print('In case you forgot to bring your own, this program simulates dice rolls.')
    print('You can even roll dies that not physically exist, such as a 38-sided die.')
    print('Here\'s how it works:')
    print('\nYou will need to enter a "code" like this:\n3d6+1, which means roll 3 six-sided dice and add one on the sum and 10d76, which rolls 10 seventy-seven sided dice. (It\'s impossible to exist!)')
    print('(The "d" character is required, the 3 in the "3d6" means "how many" and the 6 means "how many sides" and a optional modifier, either "+" or "-" to add or subtract the total by the number after the "+" or "-".)')
    print('The output:')
    print('(e.g. 3d6+4):')
    print('\n13 (3, 1, 5, +4)')
    print('\nAlright, now you know how it works and the rules, let\'s get started!')
    print('\nEnter the "code" (or QUIT to quit):')

    while True:
        try:
            dice_input = input('> ')
            dice_input = ''.join(dice_input.lower())

            if dice_input == 'quit':
                print('Thanks for playing!'); sys.exit()

            if len(dice_input) < 3:
                raise Exception('the length of the code is too short to be valid (min 3).')
            
            d_index = dice_input.find('d')
            if d_index == -1:
                raise Exception('your code is missing the "d" character (it should be in between "amount of dice" and "number of sides" like "3d6+4").')
            
            number_of_dice = dice_input[:d_index]
            if not number_of_dice.isdecimal():
                raise Exception('your "amount of dice" is not a number.')
            number_of_dice = int(number_of_dice)

            mod_index = dice_input.find('+')
            if mod_index == -1:
                mod_index = dice_input.find('-')
            
            if mod_index == -1:
                number_sides = dice_input[d_index + 1:]
            else:
                number_sides = dice_input[d_index + 1 : mod_index]
            if not number_sides.isdecimal():
                raise Exception('the "number of sides" is not a number.')
            number_sides = int(number_sides)

            if mod_index == -1:
                mod_amount = 0
            else:
                mod_amount = int(dice_input[mod_index + 1 : ])
                if dice_input[mod_index] == '-':
                    mod_amount = -mod_amount
            
            rolls = []
            for i in range(number_of_dice):
                roll_result = random.randint(1, number_sides)
                rolls.append(roll_result)
            
            print(f'\nNumber of dice: {number_of_dice}\nNumber of sides: {number_sides}\nModifier amount: {dice_input[mod_index]}{abs(mod_amount)}\nTotal: {sum(rolls) + mod_amount}\n(Each die: ', end='')
            for index, roll in enumerate(rolls):
                rolls[index] = str(roll)
            print(', '.join(rolls), end='')

            if mod_amount != 0:
                mod_sign = dice_input[mod_index]
                print(f', {mod_sign}{abs(mod_amount)}', end='')
            print(')')
            
        except Exception as exc:
            print('Your code is INVALID.')
            print(f'Your code is invalid because {str(exc)}')
            continue

if __name__ == '__main__':
    main()