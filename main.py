import os

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

# Inputting 0 in a seed will create an empty channel
# Get seed for Square1
while True:
    seed_input1 = input("Enter the seed value for Square1: ")
    try:
        # Try converting the input to an integer
        seedSquare1 = int(seed_input1)
        break  # Break out of the loop if conversion is successful
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Please enter a valid integer.")

# Get seed for Square2
while True:
    seed_input2 = input("Enter the seed value for Square2: ")
    try:
        # Try converting the input to an integer
        seedSquare2 = int(seed_input2)
        break  # Break out of the loop if conversion is successful
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Please enter a valid integer.")

# Get seed for Triangle
while True:
    seed_input3 = input("Enter the seed value for Triangle: ")
    try:
        # Try converting the input to an integer
        seedTriangle = int(seed_input3)
        break  # Break out of the loop if conversion is successful
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Please enter a valid integer.")

# Get seed for Noise
while True:
    seed_input4 = input("Enter the seed value for Noise: ")
    try:
        # Try converting the input to an integer
        seedNoise = int(seed_input4)
        break  # Break out of the loop if conversion is successful
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Please enter a valid integer.")


# Generate the sequence for each channel
generator = Base97Generator(seedSquare1)
sequenceSquare1 = generator.generate()

generator = Base97Generator(seedSquare2)
sequenceSquare2 = generator.generate()

generator = Base97Generator(seedTriangle)
sequenceTriangle = generator.generate()

generator = Base97Generator(seedNoise)
sequenceNoise = generator.generate()

# Display the sequence just in case someone can read music
print(sequenceSquare1)
print(sequenceSquare2)
print(sequenceTriangle)
print(sequenceNoise)

# Relative path to the subfolder
subfolder = "outputs"

# Get the current working directory
current_directory = os.getcwd()

# Join the current directory with the subfolder path
subfolder_path = os.path.join(current_directory, subfolder)

# Create the subfolder if it doesn't exist
if not os.path.exists(subfolder_path):
    os.makedirs(subfolder_path)

# Create a file in the subfolder and write the output
# Using four instruments to allow for instrument selection during MIDI creation
# Each channel uses 1 instrument
with open(os.path.join(subfolder_path, f"{seedSquare1}, {seedSquare2}, {seedTriangle}, {seedNoise}.txt"), "w") as file:
    file.write(f'Project Version="4.1.3" TempoMode="FamiStudio" Name="{seedSquare1}, {seedSquare2}, {seedTriangle}, '
               f'{seedNoise}" Author="Discography of Babel"\n')
    file.write('\tInstrument Name="Instrument 1"\n')
    file.write('\t\tEnvelope Type="Volume" Length="5" Values="15,10,5,1,0"\n')
    file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
    file.write('\tInstrument Name="Instrument 2"\n')
    file.write('\t\tEnvelope Type="Volume" Length="5" Values="15,10,5,1,0"\n')
    file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
    file.write('\tInstrument Name="Instrument 3"\n')
    file.write('\t\tEnvelope Type="Volume" Length="5" Values="15,10,5,1,0"\n')
    file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
    file.write('\tInstrument Name="Instrument 4"\n')
    file.write('\t\tEnvelope Type="Volume" Length="5" Values="15,10,5,1,0"\n')
    file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
    file.write(f'\tSong Name="Song {seedSquare1}, {seedSquare2}, {seedTriangle}, {seedNoise}" Length="16" LoopPoint="0"'
               f' PatternLength="16" BeatLength="4" NoteLength="10" Groove="10" GroovePaddingMode="Middle"\n')

    file.write('\t\tChannel Type="Square1"\n')
    pattern_num = 1
    for i in range(0, len(sequenceSquare1), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequenceSquare1[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 1"\n')
        pattern_num += 1
    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="Square2"\n')
    pattern_num = 1
    for i in range(0, len(sequenceSquare2), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequenceSquare2[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 2"\n')
        pattern_num += 1
    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="Triangle"\n')
    pattern_num = 1
    for i in range(0, len(sequenceTriangle), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequenceTriangle[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 3"\n')
        pattern_num += 1
    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

    file.write('\t\tChannel Type="Noise"\n')
    pattern_num = 1
    for i in range(0, len(sequenceNoise), 16):
        file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
        for j, note in enumerate(sequenceNoise[i:i + 16]):
            if note != '0':  # Check if note is not equal to '0'
                file.write(f'\t\t\t\tNote Time="{j * 10}" Value="{note}" Duration="10" Instrument="Instrument 4"\n')
        pattern_num += 1
    for i in range(16):
        file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

# DPCM channel unused
    file.write('\t\tChannel Type="DPCM"')