import dictionaries


class Base97Generator:
    def __init__(self, seed):
        self.state = seed % 2147483647  # 2**31 - 1


    def generate(self, note_numbers):
        result = []
        for _ in range(note_numbers):
            self.state = (self.state * 16807) % 2147483647  # LCG formula
            result.append(dictionaries.notes[str(self.state % 97)])  # Replace number with corresponding note
        return result
