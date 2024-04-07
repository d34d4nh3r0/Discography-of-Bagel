import os
import random


# Create a file in the output directory and write the output
# Using four instruments to allow for instrument selection during MIDI creation
# Each channel uses 1 instrument
def controlled_file_create(notes_per_beat, duration, channel_1_seed, channel_1_sequence, channel_2_seed,
                           channel_2_sequence, channel_3_seed, channel_3_sequence, channel_4_seed, channel_4_sequence):
    # Relative path to the output directory
    output_directory = "outputs"

    # Get the current working directory
    current_directory = os.getcwd()

    # Join the current directory with the output directory path
    output_directory = os.path.join(current_directory, output_directory)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Write the boring header stuff
    with open(os.path.join(output_directory, f"{channel_1_seed}, {channel_2_seed}, {channel_3_seed}, {channel_4_seed}"
                                             ".txt"), "w") as file:
        file.write(f'Project Version="4.1.3" TempoMode="FamiStudio" Name="{channel_1_seed}, {channel_2_seed}, '
                   f'{channel_3_seed}, {channel_4_seed}" Author="Discography of Babel"\n')
        file.write('\tInstrument Name="Instrument 1"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write('\tInstrument Name="Instrument 2"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write('\tInstrument Name="Instrument 3"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write('\tInstrument Name="Instrument 4"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write(f'\tSong Name="Song {channel_1_seed}, {channel_2_seed}, {channel_3_seed}, {channel_4_seed}" '
                   f'Length="16" LoopPoint="0" PatternLength="16" BeatLength="4" NoteLength="10" Groove="10" '
                   f'GroovePaddingMode="Middle"\n')

        # Write the first channel's pattern
        file.write('\t\tChannel Type="Square1"\n')
        pattern_num = 1
        for i in range(0, len(channel_1_sequence), notes_per_beat):
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            for j, note in enumerate(channel_1_sequence[i:i + notes_per_beat]):
                if note != '0':  # Check if note is not equal to '0'
                    file.write(f'\t\t\t\tNote Time="{j * duration}" Value="{note}" Duration="{duration}" Instrument='
                               f'"Instrument 1"\n')
            pattern_num += 1
        for i in range(16):
            file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

        # Write the second channel's pattern
        file.write('\t\tChannel Type="Square2"\n')
        pattern_num = 1
        for i in range(0, len(channel_2_sequence), notes_per_beat):
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            for j, note in enumerate(channel_2_sequence[i:i + notes_per_beat]):
                if note != '0':  # Check if note is not equal to '0'
                    file.write(f'\t\t\t\tNote Time="{j * duration}" Value="{note}" Duration="{duration}" Instrument='
                               f'"Instrument 2"\n')
            pattern_num += 1
        for i in range(16):
            file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

        # Write the third channel's pattern
        file.write('\t\tChannel Type="Triangle"\n')
        pattern_num = 1
        for i in range(0, len(channel_3_sequence), notes_per_beat):
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            for j, note in enumerate(channel_3_sequence[i:i + notes_per_beat]):
                if note != '0':  # Check if note is not equal to '0'
                    file.write(f'\t\t\t\tNote Time="{j * duration}" Value="{note}" Duration="{duration}" Instrument='
                               f'"Instrument 3"\n')
            pattern_num += 1
        for i in range(16):
            file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

        # Write the fourth channel's pattern
        file.write('\t\tChannel Type="Noise"\n')
        pattern_num = 1
        for i in range(0, len(channel_4_sequence), notes_per_beat):
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            for j, note in enumerate(channel_4_sequence[i:i + notes_per_beat]):
                if note != '0':  # Check if note is not equal to '0'
                    file.write(f'\t\t\t\tNote Time="{j * duration}" Value="{note}" Duration="{duration}" Instrument='
                               f'"Instrument 4"\n')
            pattern_num += 1
        for i in range(16):
            file.write(f'\t\t\tPatternInstance Time="{i}" Pattern="Pattern {i + 1}"\n')

        # DPCM channel unused
        file.write('\t\tChannel Type="DPCM"')

        print(f"{channel_1_seed}, {channel_2_seed}, {channel_3_seed}, {channel_4_seed}.txt created.")


def chaos_file_create(channel_1_seed, channel_1_sequence, channel_2_seed, channel_2_sequence, channel_3_seed,
                      channel_3_sequence, channel_4_seed, channel_4_sequence):
    # Relative path to the output directory
    output_directory = "outputs"

    # Get the current working directory
    current_directory = os.getcwd()

    # Join the current directory with the output directory path
    output_directory = os.path.join(current_directory, output_directory)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Write the boring header stuff
    with open(os.path.join(output_directory, f"{channel_1_seed}, {channel_2_seed}, {channel_3_seed}, {channel_4_seed}"
                                             ".txt"), "w") as file:
        file.write(f'Project Version="4.1.3" TempoMode="FamiStudio" Name="{channel_1_seed}, {channel_2_seed}, '
                   f'{channel_3_seed}, {channel_4_seed}" Author="Discography of Babel"\n')
        file.write('\tInstrument Name="Instrument 1"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write('\tInstrument Name="Instrument 2"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write('\tInstrument Name="Instrument 3"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write('\tInstrument Name="Instrument 4"\n')
        file.write('\t\tEnvelope Type="Volume" Length="15" Values="15,15,13,13,11,11,9,9,7,7,5,5,3,3,1"\n')
        file.write('\t\tEnvelope Type="DutyCycle" Length="1" Values="1"\n')
        file.write(f'\tSong Name="Song {channel_1_seed}, {channel_2_seed}, {channel_3_seed}, {channel_4_seed}" '
                   f'Length="16" LoopPoint="0" PatternLength="16" BeatLength="4" NoteLength="10" Groove="10" '
                   f'GroovePaddingMode="Middle"\n')

        # Write the first channel's pattern
        file.write('\t\tChannel Type="Square1"\n')
        pattern_num = 1
        max_duration = 160
        current_duration = 0
        i = 0

        while pattern_num <= 16:
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            while current_duration < max_duration:
                duration = random.randint(1, 160)
                if current_duration + duration <= max_duration:
                    note = channel_1_sequence[i]
                    current_duration = current_duration + duration
                    i += 1
                    if note != '0':  # Check if note is not equal to '0'
                        file.write(f'\t\t\t\tNote Time="{current_duration - duration}" Value="{note}" Duration='
                                   f'"{duration}" Instrument="Instrument 1"\n')
            pattern_num += 1
            current_duration = 0

        for j in range(16):
            file.write(f'\t\t\tPatternInstance Time="{j}" Pattern="Pattern {j + 1}"\n')

        # Write the second channel's pattern
        file.write('\t\tChannel Type="Square2"\n')
        pattern_num = 1
        max_duration = 160
        i = 0

        while pattern_num <= 16:
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            while current_duration < max_duration:
                duration = random.randint(1, 160)
                if current_duration + duration <= max_duration:
                    note = channel_2_sequence[i]
                    current_duration = current_duration + duration
                    i += 1
                    if note != '0':  # Check if note is not equal to '0'
                        file.write(f'\t\t\t\tNote Time="{current_duration - duration}" Value="{note}" Duration='
                                   f'"{duration}" Instrument="Instrument 2"\n')
            pattern_num += 1
            current_duration = 0

        for j in range(16):
            file.write(f'\t\t\tPatternInstance Time="{j}" Pattern="Pattern {j + 1}"\n')

        # Write the third channel's pattern
        file.write('\t\tChannel Type="Triangle"\n')
        pattern_num = 1
        max_duration = 160
        i = 0

        while pattern_num <= 16:
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            while current_duration < max_duration:
                duration = random.randint(1, 160)
                if current_duration + duration <= max_duration:
                    note = channel_3_sequence[i]
                    current_duration = current_duration + duration
                    i += 1
                    if note != '0':  # Check if note is not equal to '0'
                        file.write(f'\t\t\t\tNote Time="{current_duration - duration}" Value="{note}" Duration='
                                   f'"{duration}" Instrument="Instrument 3"\n')
            pattern_num += 1
            current_duration = 0

        for j in range(16):
            file.write(f'\t\t\tPatternInstance Time="{j}" Pattern="Pattern {j + 1}"\n')

        # Write the fourth channel's pattern
        file.write('\t\tChannel Type="Noise"\n')
        pattern_num = 1
        max_duration = 160
        i = 0

        while pattern_num <= 16:
            file.write(f'\t\t\tPattern Name="Pattern {pattern_num}"\n')
            while current_duration < max_duration:
                duration = random.randint(1, 160)
                if current_duration + duration <= max_duration:
                    note = channel_4_sequence[i]
                    current_duration = current_duration + duration
                    i += 1
                    if note != '0':  # Check if note is not equal to '0'
                        file.write(f'\t\t\t\tNote Time="{current_duration - duration}" Value="{note}" Duration='
                                   f'"{duration}" Instrument="Instrument 4"\n')
            pattern_num += 1
            current_duration = 0

        for j in range(16):
            file.write(f'\t\t\tPatternInstance Time="{j}" Pattern="Pattern {j + 1}"\n')

        # DPCM channel unused
        file.write('\t\tChannel Type="DPCM"')

        print(f"{channel_1_seed}, {channel_2_seed}, {channel_3_seed}, {channel_4_seed}.txt created.")
