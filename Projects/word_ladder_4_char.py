import sys

print('Word Ladder (4 letter), by Jayden')
print('for more information, visit https://en.wikipedia.org/wiki/Word_ladder')

# Import the file
with open('D:\配置文件\Four_letter_list.txt', "r", encoding='utf8') as file:
    wordDict = file.read().splitlines()

# # setup
# word_entered = []
# score = {}
# def check(last_one, choose, word_entered) -> bool:
#     lst = []
#     index = 0
#     for char in choose:
#         if last_one[index] == char:
#             lst.append(1)
#     if len(lst) == 3:
#         return True
#     elif len(lst) != 3:
#         return False
#     elif choose in word_entered:
#         return 0
#     elif type(choose) != str:
#         return 1
#     elif len(choose) != 4:
#         return 2

# def inputChk(Lchoose):
#     if Lchoose == 'q':
#         if score[p1t] > score[p2t]:
#             print(p1, 'wins! ')
#         elif score[p1t] == score[p2t]:
#             print('It\'s a tie! ')
#         else:
#             print(p2, 'wins! ')
#             sys.exit()
#     elif Lchoose == 'g':
#         score[p2t] += 1
#         print(p1t, ': ', score[p1t], '\n', p2t, ': ', score[p2t], sep='')

# Main
# p1 = input('Player 1, enter your name: ')
# p2 = input('Player 2, enter your name: ')
# p1t = p1.title()
# p2t = p2.title()
# score[p1t] = 0
# score[p2t] = 0
# isitp1 = True
# print(p1t, ', it\'s your turn: ', sep='')
# rawChoose = input('Enter the first word (4 letters): ')
# choose = rawChoose.upper()
# Lchoose = choose.lower()
# while Lchoose not in wordDict:
#     rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word to start: ')
#     choose = rawChoose.upper()
#     Lchoose = choose.lower()
# isitp1 = False
# word_entered.append(choose)
print('Word Ladder (4 letter), by Jayden')
print('for more information, visit https://en.wikipedia.org/wiki/Word_ladder')

# Import the file
with open('D:\配置文件\Four_letter_list.txt', "r", encoding='utf8') as file:
    wordDict = file.read().splitlines()


while True: 
    word_entered = []
    score = {}
    p1 = input('Player 1, enter your name: ')
    p2 = input('Player 2, enter your name: ')
    p1t = p1.title()
    p2t = p2.title()
    score[p1t] = 0
    score[p2t] = 0
    isitp1 = True
    print(p1t, ', it\'s your turn: ', sep='')
    rawChoose = input('Enter the first word (4 letters): ')
    choose = rawChoose.upper()
    Lchoose = choose.lower()
    while Lchoose not in wordDict:
        rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word to start: ')
        choose = rawChoose.upper()
        Lchoose = choose.lower()
    isitp1 = False
    word_entered.append(choose)

    # setup functions
    def inputChk(Lchoose):
        if Lchoose == 'q':
            if score[p1t] > score[p2t]:
                print(p1, 'wins! ')
            elif score[p1t] == score[p2t]:
                print('It\'s a tie! ')
            else:
                print(p2, 'wins! ')
                sys.exit()
        elif Lchoose == 'g':
            score[p2t] += 1
            print(p1t, ': ', score[p1t], '\n', p2t, ': ', score[p2t], sep='')
            pass
    def check(last_one, choose, word_entered) -> bool:
        lst = []
        index = 0
        for char in choose:
            if last_one[index] == char:
                lst.append(1)
        if len(lst) == 3:
            return True
        elif len(lst) != 3:
            return False
        elif choose in word_entered:
            return 0
        elif type(choose) != str:
            return 1
        elif len(choose) != 4:
            return 2

    # main game loop starts
    if isitp1 == True:
        print('\n' * 40) # 'clear' the screen
        for item in word_entered:
            print(item)
        print(p1t, ', is\'s your turn. ', sep='', end='')
        rawChoose = input('Enter the next word (q to quit and g for give up): ')
        choose = rawChoose.upper()
        Lchoose = choose.lower()
        inputChk(Lchoose)
        while Lchoose not in wordDict:
            rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word: ')
            choose = rawChoose.upper()
            Lchoose = choose.lower()
        last_one = word_entered[-1]
        result = check(last_one, choose, word_entered)

        if result == True:
            pass
        while result == False:
            # while len(ifitsgood) != 3:
            print('This is not the right word. The difference between the last one and yours should be one letter.')
            rawChoose = input('Enter a word that follows the rules (q to quit and g for give up): ')
            choose = rawChoose.upper()
            Lchoose = choose.lower()
        while result == 0:
            print('The word you choose is already entered.')
            rawChoose = input('Enter a word that follows the rules (q to quit and g for give up): ')
            choose = rawChoose.upper()
            Lchoose = choose.lower()
            choose = rawChoose.upper()
            Lchoose = choose.lower()
            # if Lchoose == 'q':
            #     if score[p1t] > score[p2t]:
            #         print(p1, 'wins! ')
            #     elif score[p1t] == score[p2t]:
            #         print('It\'s a tie! ')
            #     else:
            #         print(p2, 'wins! ')
            #     sys.exit()
            # elif Lchoose == 'g':
            #     score[p2t] += 1
            #     print(p1t, ': ', score[p1t], '\n', p2t, ': ', score[p2t], sep='')
            #     continue
            inputChk(Lchoose)
        word_entered.append(choose)
        isitp1 = False

    elif isitp1 == False:
        print('\n' * 40) # 'clear' the screen
        for item in word_entered:
            print(item)
        print(p2t, ', it\'s your turn. ', sep='', end='')
        rawChoose = input('Enter the next word (q to quit and g to give up): ')
        choose = rawChoose.upper()
        Lchoose = choose.lower()
        # if Lchoose == 'q':
        #     if score[p1t] > score[p2t]:
        #         print(p1, 'wins! ')
        #     elif score[p1t] == score[p2t]:
        #         print('It\'s a tie! ')
        #     else:
        #         print(p2, 'wins! ')
        #     sys.exit()
        # elif Lchoose == 'g':
        #     score[p1t] += 1
        #     print(p1t, ': ', score[p1t], '\n', p2t, ': ', score[p2t], sep='')
        #     continue
        inputChk(Lchoose)
        while Lchoose not in wordDict:
            rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word (q to quit and g to give up): ')
            choose = rawChoose.upper()
            Lchoose = choose.lower()
        last_one = word_entered[-1]
        ifitsgood = []
        check(last_one, choose, word_entered)

        # letter1 = choose[0]
        # letter2 = choose[1]
        # letter3 = choose[2]
        # letter4 = choose[3]
        
        # if last_one[0] == letter1:
        #     ifitsgood.append(1)
        # if last_one[1] == letter2:
        #     ifitsgood.append(1)
        # if last_one[2] == letter3:
        #     ifitsgood.append(1)
        # if last_one[3] == letter4:
        #     ifitsgood.append(1)
        
        # if len(ifitsgood) == 3:
        #     pass
        # while len(ifitsgood) != 3 or last_one == choose or choose in word_entered or len(choose) != 4:
        #     while len(ifitsgood) != 3:
        #         print('This is not the right word. The difference between the last one and yours should be one letter.')
        #         rawChoose = input('Enter a word that follows the rules (q to quit and g for give up): ')
        #         choose = rawChoose.upper()
        #         Lchoose = choose.lower()
        #     while choose in word_entered:
        #         print('The word you choose is already entered.')
        #         rawChoose = input('Enter a word that follows the rules (q to quit and g for give up): ')
        #         choose = rawChoose.upper()
        #         Lchoose = choose.lower()
        choose = rawChoose.upper()
        Lchoose = choose.lower()
        # if Lchoose == 'q':
        #     if score[p1t] > score[p2t]:
        #         print(p1, 'wins! ')                
        #     elif score[p1t] == score[p2t]:
        #             print('It\'s a tie! ')
        #     else:
        #             print(p2, 'wins! ')
        #     sys.exit()
        # elif Lchoose == 'g':
        #     score[p1t] += 1
        #     print(p1t, ': ', score[p1t], '\n', p2t, ': ', score[p2t], sep='')
        #     continue
        inputChk(Lchoose)
        word_entered.append(choose)
        isitp1 = True



## custom difference() function that takes in two strings and returns false if
## difference between strings is greater than 1 or equals zero
## player could input 'g' for giving up, or 's' to view score, or 'q' to quit

# def difference (str1, str2) -> bool:
#     diff = 0
#     for i in range(0, len(str1)):
#         if str1[i] != str2[i]:
#             diff += 1
#         if diff > 1:
#             return False
#     if diff == 0:
#         return False
#     return True

# print('Word Ladder (4 letter), by Jayden')
# print('for more information, visit https://en.wikipedia.org/wiki/Word_ladder')

# import sys
# # BY Joyce:
# with open('four_letter.txt', "r", encoding='utf8') as file:
#     wordDict = file.read().splitlines()

# p1 = input('Player 1, enter your name: ')
# p2 = input('Player 2, enter your name: ')
# p1T = p1.title()
# p2T = p2.title()
# score = dict()
# isitp1 = True
# print(p1T, ', it\'s your turn: ', sep='')
# rawChoose = input('Enter the first word (4 letters): ')
# choose = rawChoose.upper()
# Lchoose = choose.lower()
# while Lchoose not in wordDict:
#     rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word to start: ')
#     choose = rawChoose.upper() 
#     Lchoose = choose.lower() 
# isitp1 = False
# print(choose)
# prev = choose

# while True:
#     if isitp1 == True:
#         print(p1T, ', is\'s your turn. ', sep='', end='')
#         rawChoose = input('Enter the next word (or: Q for quit, S for viewing score table, G for give up): ')
#         choose = rawChoose.upper()
#         Lchoose = choose.lower()
#         if Lchoose == 'q':
#             sys.exit()
#         while Lchoose not in wordDict and Lchoose != 'g' and Lchoose != 's':
#             rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word: ')
#             choose = rawChoose.upper() 
#             Lchoose = choose.lower() 
#         if Lchoose == 'g': 
#             score[p1T] = score.get(p1T, 0) + 1
#             isitp1 = False
#             continue
#         if Lchoose == 's':
#             print(score)
#             choose = prev
#             continue

#         if difference(prev, choose):
#             score[p1T] = score.get(p1T, 0) + 1
#         else:
#             print('This is not the right word. The difference between the last one and yours should be one letter. The next player continues.')
#             isitp1 = False
#             continue

#         sys.stdout.write("\033[F")
#         sys.stdout.write("\033[K")
#         sys.stdout.write('\r' + choose + '\n')
#         prev = choose
        
#         isitp1 = False
#     elif isitp1 == False:
#         print(p2T, ', is\'s your turn. ', sep='', end='')
#         rawChoose = input('Enter the next word (or: Q for quit, S for viewing score table, G for give up): ')
#         choose = rawChoose.upper()
#         Lchoose = choose.lower()
#         if Lchoose == 'q':
#             sys.exit()
#         while Lchoose not in wordDict and Lchoose != 'g' and Lchoose != 's':
#             rawChoose = input('This is not a valid 4 letter word. Enter a valid 4 letter word: ')
#             choose = rawChoose.upper() 
#             Lchoose = choose.lower() 
#         if Lchoose == 'g': 
#             score[p2T] = score.get(p2T, 0) + 1
#             isitp1 = True
#             continue
#         if Lchoose == 's':
#             print(score)
#             choose = prev
#             continue
        
#         if difference(prev, choose):
#             score[p2T] = score.get(p2T, 0) + 1
#         else:
#             print('This is not the right word. The difference between the last one and yours should be one letter. The next player continues.')
#             isitp1 = True
#             continue

#         sys.stdout.write("\033[F")
#         sys.stdout.write("\033[K")
#         sys.stdout.write('\r' + choose + '\n')
#         prev = choose
    
#         isitp1 = True

