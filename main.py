class Base97Generator:
    def __init__(self, seed):
        self.state = seed % 2147483647  # 2**31 - 1

    def generate(self):
        result = []
        for _ in range(256):
            self.state = (self.state * 16807) % 2147483647  # LCG formula
            result.append(notes[str(self.state % 97)])  # Replace number with corresponding note
        return result


# Creating a dictionary to go from 97 to FamiStudio note
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

while True:
    seed_input = input("Enter the seed value: ")
    try:
        # Try converting the input to an integer
        seed = int(seed_input)
        break  # Break out of the loop if conversion is successful
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Please enter a valid integer.")

# Generate the song
generator = Base97Generator(seed)
sequence = generator.generate()

# Display the sequence just in case
print(sequence)

# Create a file and write the output
with open(f"{seed}.txt", "w") as file:
    file.write(f'Project Version="4.1.3" TempoMode="FamiStudio" Name="{seed}" Author="Discography of Babel"\n')
    file.write('\tInstrument Name="Instrument 1"\n')
    file.write('\t\tEnvelope Type="Volume" Length="5" Values="15,10,5,1,0"\n')
    file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
    file.write(f'\tSong Name="Song {seed}" Length="16" LoopPoint="0" PatternLength="16" BeatLength="4" NoteLength="10" Groove="10" GroovePaddingMode="Middle"\n')
    file.write('\t\tChannel Type="Square1"\n')

    pattern_num = 1
    for i in range(0, len(sequence), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequence[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 1"\n')
        pattern_num += 1

    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="Square2"\n')

    pattern_num = 1
    for i in range(0, len(sequence), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequence[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 1"\n')
        pattern_num += 1

    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="Triangle"\n')

    pattern_num = 1
    for i in range(0, len(sequence), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequence[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 1"\n')
        pattern_num += 1

    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="Noise"\n')

    pattern_num = 1
    for i in range(0, len(sequence), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequence[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 1"\n')
        pattern_num += 1

    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="DPCM"')

    # Testing Git change