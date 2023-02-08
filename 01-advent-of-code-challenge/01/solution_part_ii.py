def get_first_tree_max_group(file):
    lines = file.readlines()
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


print(get_first_tree_max_group(open("sample.in")))
