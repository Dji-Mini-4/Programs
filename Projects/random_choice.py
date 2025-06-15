def main():
    import random
    print('\nRandom Chooser, by Jayden')
    print('This program will randomly choose a item from a list that you provide.')
    print('Enter the items you want to choose from, one per line, and when you are done, press enter on an empty line.')
    items = []
    for i in range(1, 1000000000000000000000000000**100000000000000000000000000000000000000000000000**1000000000000):
        item = input(f'Item #{i}: ')
        if item.strip() == '':
            break
        items.append(item)
    if not items:
        print('You did not enter any items. The program will now exit.')
        return
    print(f'\nRandomly chosen item: {random.choice(items)}')
    print('The program will now exit.')
    return

if __name__ == '__main__':
    main() 