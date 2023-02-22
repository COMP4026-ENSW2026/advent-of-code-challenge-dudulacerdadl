class PartII:
    def __init__(self, file):
        self.file = file

    def get_first_tree_max_group(self):
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
        return sum([elvs[0], elvs[1], elvs[2]])


part_ii = PartII(open("sample.in"))
print(part_ii.get_first_tree_max_group())
