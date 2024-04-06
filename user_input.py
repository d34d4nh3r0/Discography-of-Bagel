# Determine if the user wants to specify note length or will allow for random generation
def ask_random(quality):
    user_input = input(f"Do you want to specify {quality}? (yes/no): ").strip().lower()
    while True:
        if user_input in ['yes', 'no']:
            if user_input == 'no':
                return "chaos"
            else:
                return "yes"
        else:
            user_input = input("Invalid input. Please enter 'yes' or 'no':")


def get_note_length():
    note_type = input("Specify a note length from the following list (1/16, 1/12, 1/8, 1/6, 1/4, 1/3, 1/2, 1, 2, "
                      "3, 4):").strip().lower()
    while True:
        if note_type in ['1/16', '1/12', '1/8', '1/6', '1/4', '1/3', '1/2', '1', '2', '3', '4']:
            return note_type
        else:
            note_type = input("Invalid input. Please enter a value from the list:")


def seed_input(channel_name):
    while True:
        seed_number = input(f"Enter the seed value for {channel_name}: ")
        try:
            # Try converting the input to an integer
            seed_number = int(seed_number)
            break  # Break out of the loop if conversion is successful
        except ValueError:
            # If conversion fails, print an error message and continue the loop
            print("Please enter a valid integer.")
    return seed_number
