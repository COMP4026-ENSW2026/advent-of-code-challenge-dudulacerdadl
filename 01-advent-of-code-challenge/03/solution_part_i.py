class PartI:
    def __init__(self, file):
        self.file = file

    def get_result_points(self):
        lines = self.file.readlines()
        iquals = []
        for line in lines:
            half = len(line) // 2
            first_half = line[:half]
            second_half = line[half:]

            for string in first_half:
                if string in second_half:
                    if string.isupper():
                        iquals.append(self.validate_upper(string))
                    else:
                        iquals.append(self.validate_lower(string))
                    break

        return sum(iquals)

    def validate_upper(self, string):
        return ord(string) - 38

    def validate_lower(self, string):
        return ord(string) - 96


part_i = PartI(open("input.txt"))
print(part_i.get_result_points())
