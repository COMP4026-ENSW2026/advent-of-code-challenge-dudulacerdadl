class PartII:
    def __init__(self, file):
        self.file = file

    def get_result_points(self):
        lines = self.file.readlines()
        iquals = []
        groups = []
        aux = []
        for line in lines:
            aux.append(line)
            if len(aux) >= 3:
                groups.append(aux)
                aux = []

        for group in groups:
            for string in group[0]:
                if string in group[1] and string in group[2]:
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


part_ii = PartII(open("input.txt"))
print(part_ii.get_result_points())
