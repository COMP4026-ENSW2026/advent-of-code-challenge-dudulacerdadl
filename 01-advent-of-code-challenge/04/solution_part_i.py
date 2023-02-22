class PartI:
    def __init__(self, file):
        self.file = file

    def get_subsets(self):
        lines = self.file.readlines()
        pairs = 0
        for line in lines:
            aux = line.split(",")
            first_pair = set(self.get_numeric_list(aux[0].split("-")))
            secund_pair = set(self.get_numeric_list(aux[1].rstrip().split("-")))
            if (first_pair <= secund_pair) or (secund_pair <= first_pair):
                pairs += 1
        return pairs

    def get_numeric_list(self, pair):
        numeric_list = []
        for num in range(int(pair[0]), int(pair[1]) + 1):
            numeric_list.append(num)

        return numeric_list


part_i = PartI(open("input.txt"))
print(part_i.get_subsets())
