class PartII:
    def __init__(self, file):
        self.file = file

    def get_result_points(self):
        lines = self.file.readlines()
        result = 0
        for line in lines:
            oponent = line[0]
            your = line[2]

            if your == 'X':
                result += 0 + self.defeats(oponent)
            if your == 'Y':
                result += 3 + self.draws(oponent)
            if your == 'Z':
                result += 6 + self.victories(oponent)

        return result

    def victories(self, oponent):
        if oponent == 'A':
            return 2
        if oponent == 'B':
            return 3
        if oponent == 'C':
            return 1

    def draws(self, oponent):
        if oponent == 'A':
            return 1
        if oponent == 'B':
            return 2
        if oponent == 'C':
            return 3

    def defeats(self, oponent):
        if oponent == 'A':
            return 3
        if oponent == 'B':
            return 1
        if oponent == 'C':
            return 2


part_ii = PartII(open("input.txt"))
print(part_ii.get_result_points())
