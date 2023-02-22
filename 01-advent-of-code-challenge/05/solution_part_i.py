class PartI:
    def __init__(self, file):
        self.file = file

    def get_top_stack(self):
        lines = self.file.readlines()
        rules = []
        order = []
        size = int(len(lines[0]) / 4)
        for line in lines:
            if line[0] == 'm':
                rules.append(self.set_rules(line))
            if '[' in line:
                count = 0
                while count < size:
                    index = count * 4 + 1
                    try:
                        order[count].append(line[index])
                    except IndexError:
                        order.append([line[index]])
                    count += 1

        for i, items in enumerate(order):
            aux_array = self.remove_from_array(items, ' ')
            order[i] = aux_array[::-1]

        for rule in rules:
            qty = rule[0] * -1
            origin = rule[1] - 1
            destiny = rule[2] - 1

            moved = order[origin][qty:][::-1]
            print('----------')
            print(f'Qty: {qty}\nOrigin: {origin}\nDestiny: {destiny}\nMoved: {moved}')
            print('----------')
            if moved == []:
                return
            for item in moved:
                order[origin].remove(item)
                order[destiny].append(item)

        print(order)
        result = []
        for item in order:
            if len(item) != 0:
                result.append(item[-1])
            else:
                result.append(' ')

        return "".join(result)

    def set_rules(self, line):
        line = line.rstrip().split(' ')
        numbers = []
        for string in line:
            if string.isdigit():
                numbers.append(int(string))
        return numbers

    def remove_from_array(self, origin_array, removed):
        return [
            array for array in origin_array if removed not in array
        ]

part_i = PartI(open("input.txt"))
# part_i = PartI(open("sample.in"))
print(part_i.get_top_stack())
