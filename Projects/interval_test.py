import os
import random
import time

try:
    import playsound
except ImportError:
    print('You\'ll need the playsound module in order to make this program work.')
    quit()

print('Interval Test, by Jayden')
print('This program tests your ability to identify musical intervals.')

folder_path = 'D:\\Setup\\Setup_Files\\piano_notes'
filenames = os.listdir(folder_path)
notes = [filename.rstrip('.mp3') for filename in filenames]

interval_names = [
    "minor 2nd", "major 2nd", "minor 3rd", "major 3rd",
    "perfect 4th", "tritone", "perfect 5th", "minor 6th",
    "major 6th", "minor 7th", "major 7th", "perfect 8ve"
]
note_order = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_to_midi(note_name):
    # Accepts formats like C4, Db4, Eb10, etc.
    if len(note_name) < 2:
        return None
    name = note_name[0]
    if note_name[1] == 'b':
        accidental = 'b'
        octave = note_name[2:]
    else:
        accidental = ''
        octave = note_name[1:]
    try:
        octave = int(octave)
    except ValueError:
        return None
    if accidental == 'b':
        idx = (note_order.index(name) - 1) % 12
    else:
        idx = note_order.index(name)
    return 12 * (octave + 1) + idx

print('\n****ENTERING**INTERVAL*TEST**MODE****')
# Build a dict of midi -> note_name for all available notes in range
midi_to_name = {}
for n in notes:
    midi = note_to_midi(n)
    if midi is not None and 48 <= midi <= 84:
        midi_to_name[midi] = n

midi_notes = sorted(midi_to_name.keys())
while True:
    # Pick a random starting note and interval
    start_midi = random.choice(midi_notes)
    # Only allow intervals that fit within available notes and stay in range
    possible_intervals = [i for i in range(1, 13) if (start_midi + i) in midi_to_name]
    if not possible_intervals:
        continue
    interval = random.choice(possible_intervals)
    end_midi = start_midi + interval
    start_note = midi_to_name[start_midi]
    end_note = midi_to_name[end_midi]
    print('\nListen to the interval:')
    playsound.playsound(os.path.join(folder_path, start_note + '.mp3'))
    time.sleep(0.5)
    playsound.playsound(os.path.join(folder_path, end_note + '.mp3'))
    print('What is the interval? (e.g. minor 2nd, major 3rd, perfect 5th, perfect 8ve)')
    answer = input('> ').strip().lower()
    correct = interval_names[interval - 1]
    if answer == correct:
        print('Correct!')
    else:
        print(f'Incorrect. The answer was: {correct}')
    again = input('Press Enter to try another, or type QUIT to exit: ').strip().upper()
    if again == 'QUIT':
        break