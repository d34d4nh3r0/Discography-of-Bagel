import file_generation
import user_input
import random
import dictionaries
import note_generation

# Get first user decision - controlled or random generation
note_control = user_input.ask_random("note length")

# Branch if controlled generation
if note_control == "yes":
    note_length = user_input.get_note_length()
    seed_control = user_input.ask_random("channel seeds")
    if seed_control == "yes":
        square1_seed = user_input.seed_input("Square1")
        square2_seed = user_input.seed_input("Square2")
        triangle_seed = user_input.seed_input("Triangle")
        noise_seed = user_input.seed_input("Noise")
    else:
        square1_seed = random.randint(0, 18446744073709551615)
        square2_seed = random.randint(0, 18446744073709551615)
        triangle_seed = random.randint(0, 18446744073709551615)
        noise_seed = random.randint(0, 18446744073709551615)
    note_duration = int(dictionaries.note_durations[note_length])
    total_notes = int(dictionaries.note_numbers[note_length])
    notes_per_beat = int(dictionaries.notes_per_beat[note_length])

    # Generate the sequence for each channel
    generator = note_generation.Base97Generator(square1_seed)
    square1_sequence = generator.generate(total_notes)

    generator = note_generation.Base97Generator(square2_seed)
    square2_sequence = generator.generate(total_notes)

    generator = note_generation.Base97Generator(triangle_seed)
    triangle_sequence = generator.generate(total_notes)

    generator = note_generation.Base97Generator(noise_seed)
    noise_sequence = generator.generate(total_notes)

    # Display the sequence just in case someone can read music
    print(square1_sequence)
    print(square2_sequence)
    print(triangle_sequence)
    print(noise_sequence)

    # Pass off all the information we've gained into the file writing portion
    file_generation.controlled_file_create(notes_per_beat, note_duration, square1_seed, square1_sequence, square2_seed,
                                           square2_sequence, triangle_seed, triangle_sequence, noise_seed,
                                           noise_sequence)

else:
    seed_control = user_input.ask_random("channel seeds")

    if seed_control == "yes":
        square1_seed = user_input.seed_input("Square1")
        square2_seed = user_input.seed_input("Square2")
        triangle_seed = user_input.seed_input("Triangle")
        noise_seed = user_input.seed_input("Noise")
    else:
        square1_seed = random.randint(0, 18446744073709551615)
        square2_seed = random.randint(0, 18446744073709551615)
        triangle_seed = random.randint(0, 18446744073709551615)
        noise_seed = random.randint(0, 18446744073709551615)

    # Generate the sequence for each channel
    generator = note_generation.Base97Generator(square1_seed)
    square1_sequence = generator.generate(2560)

    generator = note_generation.Base97Generator(square2_seed)
    square2_sequence = generator.generate(2560)

    generator = note_generation.Base97Generator(triangle_seed)
    triangle_sequence = generator.generate(2560)

    generator = note_generation.Base97Generator(noise_seed)
    noise_sequence = generator.generate(2560)

    # Display the sequence just in case someone can read music
    print(square1_sequence)
    print(square2_sequence)
    print(triangle_sequence)
    print(noise_sequence)

    # Pass off all the information we've gained into the file writing portion
    file_generation.chaos_file_create(square1_seed, square1_sequence, square2_seed, square2_sequence, triangle_seed,
                                      triangle_sequence, noise_seed, noise_sequence)
