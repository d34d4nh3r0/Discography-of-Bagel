# Dictionary to convert the base97 number to FamiStuido note
notes = {'0': '0', '1': 'C0', '2': 'C#0', '3': 'D0', '4': 'D#0', '5': 'E0', '6': 'F0', '7': 'F#0', '8': 'G0',
         '9': 'G#0', '10': 'A0', '11': 'A#0', '12': 'B0', '13': 'C1', '14': 'C#1', '15': 'D1', '16': 'D#1',
         '17': 'E1', '18': 'F1', '19': 'F#1', '20': 'G1', '21': 'G#1', '22': 'A1', '23': 'A#1', '24': 'B1',
         '25': 'C2', '26': 'C#2', '27': 'D2', '28': 'D#2', '29': 'E2', '30': 'F2', '31': 'F#2', '32': 'G2',
         '33': 'G#2', '34': 'A2', '35': 'A#2', '36': 'B2', '37': 'C3', '38': 'C#3', '39': 'D3', '40': 'D#3',
         '41': 'E3', '42': 'F3', '43': 'F#3', '44': 'G3', '45': 'G#3', '46': 'A3', '47': 'A#3', '48': 'B3',
         '49': 'C4', '50': 'C#4', '51': 'D4', '52': 'D#4', '53': 'E4', '54': 'F4', '55': 'F#4', '56': 'G4',
         '57': 'G#4', '58': 'A4', '59': 'A#4', '60': 'B4', '61': 'C5', '62': 'C#5', '63': 'D5', '64': 'D#5',
         '65': 'E5', '66': 'F5', '67': 'F#5', '68': 'G5', '69': 'G#5', '70': 'A5', '71': 'A#5', '72': 'B5',
         '73': 'C6', '74': 'C#6', '75': 'D6', '76': 'D#6', '77': 'E6', '78': 'F6', '79': 'F#6', '80': 'G6',
         '81': 'G#6', '82': 'A6', '83': 'A#6', '84': 'B6', '85': 'C7', '86': 'C#7', '87': 'D7', '88': 'D#7',
         '89': 'E7', '90': 'F7', '91': 'F#7', '92': 'G7', '93': 'G#7', '94': 'A7', '95': 'A#7', '96': 'B7'}

# Dictionary to derive the duration of the note based on note length
note_durations = {'1/16': '3', '1/12': '4', '1/8': '5', '1/6': '7', '1/4': '10', '1/3': '14', '1/2': '20', '1': '40',
                  '2': '80', '3': '120', '4': '160'}

# Dictionary to derive the number of notes needed to fill the song based on note length
note_numbers = {'1/16': '848', '1/12': '640', '1/8': '512', '1/6': '352', '1/4': '256', '1/3': '176', '1/2': '128',
                '1': '64', '2': '32', '3': '16', '4': '16'}

# Dictionary to derive number of notes to pattern based on note length
notes_per_beat = {'1/16': '64', '1/12': '48', '1/8': '32', '1/6': '24', '1/4': '16', '1/3': '12', '1/2': '8', '1': '4',
                  '2': '2', '3': '1', '4': '1'}
