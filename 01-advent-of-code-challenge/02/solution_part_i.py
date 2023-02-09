# A = Pedra
# B = Papel
# C = Tesoura
# ---
# X = Papel -> 2
# Y = Pedra -> 1
# Z = Tesoura -> 3
# ---
# Derrota = 0
# Empate = 3
# Vitória = 6

class PartI:
    def __init__(self, file):
        self.file = file

    def get_result_points(self):
        lines = self.file.readlines()
        for line in lines:
            if line == '\n':
                continue
            line = int(line.split('\n')[0])
            game = []
