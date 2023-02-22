class PartI:
    def __init__(self, file):
        self.file = file

    def get_max_group(self):
        lines = self.file.readlines()
        elvs = []
        aux_elv = []
        for line in lines:
            if line == '\n':
                elvs.append(sum(aux_elv))
                aux_elv = []
                continue
            line = int(line.split('\n')[0])
            aux_elv.append(line)

        elvs.sort(reverse=True)
        return elvs[0]


part_i = PartI(open("sample.in"))
print(part_i.get_max_group())
