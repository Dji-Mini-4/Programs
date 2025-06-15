import os
import time

try:
    import playsound
except ImportError:
    print('You\'ll need the playsound module in order to make this program work.')
    quit()

print('Hear Notes, by Jayden')
print('This program lets you hear any piano note in your collection.')

folder_path = 'D:\\Setup\\Setup_Files\\piano_notes'
filenames = os.listdir(folder_path)
notes = [filename.rstrip('.mp3') for filename in filenames]

# Map for next/previous note for sharp/flat logic
note_order = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
note_index = {n: i for i, n in enumerate(note_order)}

while True:
    print('\nEnter the note NAME (A,B,C,D,E,F,G), or QUIT to exit:')
    note_name = input('> ').upper()
    if note_name == 'QUIT':
        break
    if note_name not in note_order:
        print('That\'s invalid. Enter one of A,B,C,D,E,F,G.')
        continue

    print('Enter "b" if flat, "s" if sharp, or press Enter if natural:')
    accidentals = input('> ').lower()
    if accidentals not in ('', 'b', 's'):
        print('That\'s not valid. Enter "b" if flat, "s" if sharp, or press Enter if natural.')
        continue

    print('Enter the note\'s OCTAVE (0-8):')
    note_octave = input('> ')
    if not note_octave.isnumeric() or not (0 <= int(note_octave) <= 8):
        print('That\'s not valid.')
        continue
    note_octave = int(note_octave)

    # Handle special enharmonic cases
    if accidentals == 's':
        if note_name == 'E':
            form_note_name = f'F{note_octave}'
            print(f'Transforming "E#{note_octave}" into "F{note_octave}"...')
            time.sleep(0.5)
        elif note_name == 'B':
            # B# is C of next octave
            if note_octave == 8:
                print('B#8 is out of range on an 88-key piano.')
                continue
            form_note_name = f'C{note_octave+1}'
            print(f'Transforming "B#{note_octave}" into "C{note_octave+1}"...')
            time.sleep(0.5)
        else:
            # Regular sharp: next note as flat
            idx = note_index[note_name]
            next_note = note_order[(idx + 1) % 7]
            next_octave = note_octave + 1 if note_name == 'B' else note_octave
            form_note_name = f'{next_note}b{next_octave}'
            print(f'Transforming "{note_name}#{note_octave}" into "{next_note}b{next_octave}"...')
            time.sleep(0.5)
    elif accidentals == 'b':
        if note_name == 'C':
            # Cb is B of previous octave
            if note_octave == 0:
                print('Cb0 is out of range on an 88-key piano.')
                continue
            form_note_name = f'B{note_octave-1}'
            print(f'Transforming "Cb{note_octave}" into "B{note_octave-1}"...')
            time.sleep(0.5)
        elif note_name == 'F':
            # Fb is E of same octave
            form_note_name = f'E{note_octave}'
            print(f'Transforming "Fb{note_octave}" into "E{note_octave}"...')
            time.sleep(0.5)
        else:
            # Regular flat: previous note
            idx = note_index[note_name]
            prev_note = note_order[(idx - 1) % 7]
            prev_octave = note_octave - 1 if note_name == 'C' else note_octave
            form_note_name = f'{prev_note}{prev_octave}'
            print(f'Transforming "{note_name}b{note_octave}" into "{prev_note}{prev_octave}"...')
            time.sleep(0.5)
    else:
        form_note_name = f'{note_name}{note_octave}'

    if form_note_name in notes:
        official_notenm = form_note_name + '.mp3'
        print(f'Playing {official_notenm}...')
        playsound.playsound(os.path.join(folder_path, official_notenm))
    else:
        print(f'Note {form_note_name} not found in available notes.')