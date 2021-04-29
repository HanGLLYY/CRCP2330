  
from enum import Enum
class Parser:
    
    class CommandType(Enum):
        A_COMMAND = 1
        C_COMMAND = 2
        L_COMMAND = 3
    
    def __init__(self, asm):
        self.commands = []
        with open(asm, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not self.is_comment(line):
                    self.commands.append(line)
                    

    def is_comment(self, line):
        return line.startswith('//')
    
if __name__ == '__main__':
    parser = Parser('Add.asm')
    print(parser.commands)
    print(list(Parser.CommandType))