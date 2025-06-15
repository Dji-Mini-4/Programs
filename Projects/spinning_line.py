'''A simple program that displays a spinning line.'''

import time, os

spin_lst = [
    '''
     |
     |
     |
     |
     |
''', 

'''
      /
     /
    /
   /
  /
''', 

'''


----------


''', 

'''
  \ 
   \ 
    \ 
     \ 
      \ 
'''
]

print('Spinning Line, by Jayden')
input('Press Enter to start, Ctrl-C to quit...')

while True:
    try:
        for line in spin_lst:
            os.system('cls')
            print('\n\n\n\n\n')
            print(line)
            time.sleep(0.08)
    except KeyboardInterrupt:
        os.system('cls')
        print('\n' * 50)
        print('_____FINISHED_EXECUTING_____\n\n')
        break