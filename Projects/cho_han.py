print('''Cho-Han, the traditional Japanese dice game of even-odd.

In this Japanese game, two dice are rolled in a bamboo cup by the dealer sitting on the floor. The player must guess if the dice total to an even (cho) or odd (han) number.
''')      

import random, sys

JAPANESE_NUMBER = {1:"ICHI", 2:"NI", 3:"SAN", 4:"YON", 5:"GO", 6:"ROKU"}

purse = 5000

while True:    #main game loop.
    #place your bet:
    print("You have", purse, "mon. How much do you bet? (or QUIT)")
    while True:
        pot = input(">")
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            #this is a valid bet.
            pot = int(pot) # convert pot to an integer.
            break

    #roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams the cup on the floor, still covering the ")
    print("dice and asks for your bet.")
    print()
    print("CHO (even) or HAN (odd)?")

    #Let the player bet cho or han:
    while True:
        bet = input("> ").upper()
        if bet != "CHO" and bet != "HAN" :
            print("Please enter either 'CHO' or 'HAN'. ")
            continue
        else:
            break

    #reveal the dice results:
    print("The dealer lifts up the cup to reveal: ")
    print("    ", JAPANESE_NUMBER[dice1], "-", JAPANESE_NUMBER[dice2])
    print("       ", dice1, "-", dice2)

    # Determine if the player won:
    rolliseven = (dice1 + dice2) % 2 == 0
    if rolliseven :
        correctBet = "CHO"
    else:
        correctBet = "HAN"

    playerWon = bet == correctBet

    # Display the best results:
    if playerWon:
        print("You won! You take", pot, "mon.")
        purse = purse + pot
        print("The house collects a", pot // 10, "mon fee.")
        purse = purse - (pot // 10)
    else:
        print("You lost!")
        purse = purse - pot

    if purse == 0:
        print("You have run out of money!")
        print("Thanks for playing!")
        sys.exit()

