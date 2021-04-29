
class Parser:
    def __init__(self, asm):
        self.lines = []
        with open(asm, 'r') as f:
            for line in f:
                self.lines.append(line.strip())

if __name__ == '__main__':
    parser = Parser('Add.asm')
    print(parser.lines)
