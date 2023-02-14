class PartI:
    def __init__(self, file):
        self.file = file

    def get_result_points(self):
        lines = self.file.readlines()
        result = 0
        for line in lines:
            oponent = line[0]
            your = line[2]

            if your == 'X':
                result += 1

            if your == 'Y':
                result += 2

            if your == 'Z':
                result += 3

            result += self.combat(oponent, your)

        return result

    def combat(self, oponent, your):
        result = 0
        if (oponent == 'A' and your == 'Z') or (oponent == 'B' and your == 'X') or (oponent == 'C' and your == 'Y'):
            result = 0

        if (oponent == 'A' and your == 'X') or (oponent == 'B' and your == 'Y') or (oponent == 'C' and your == 'Z'):
            result = 3

        if (oponent == 'A' and your == 'Y') or (oponent == 'B' and your == 'Z') or (oponent == 'C' and your == 'X'):
            result = 6

        return result


part_i = PartI(open("input.txt"))
print(part_i.get_result_points())
