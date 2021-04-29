import code
import Parser
import Code

class Assembler:
    def __init__(self, asm):
        self.parser = Parser.Parser(asm)
        self.symbol_table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }
        for r in range(16):
            self.symbol_table['R{}'.format(r)] = r
            
    def build_symbol_table(self):
        addr = 0
        for cmd in self.parser.commands:
            cmd_type = self.parser.command_type(cmd)
            if cmd_type == Parser.CommandType.L_COMMAND:
                sym = self.parser.symbol(cmd)
                self.symbol_table[sym] = addr
            else:
                addr += 1

        addr = 16
        for cmd in self.parser.commands:
            if cmd_type == Parser.CommandType.A_COMMAND:
                sym = self.parser.symbol(cmd)
                try:
                    int(sym)
                except:
                    if sym not in self.symbol_table:
                        self.symbol_table[sym] = addr
                        addr += 1

    def assemble(self):
        self.build_symbol_table()
        codes = []
        for cmd in self.parser.commands:
            cmd_type = self.parser.command_type(cmd)
            if cmd_type == Parser.CommandType.C_COMMAND:
                dest = Code.dest(self.parser.dest(cmd))
                comp = Code.comp(self.parser.comp(cmd))
                jump = Code.jump(self.parser.jump(cmd))
                codes.append('111' + comp + dest + jump)
            elif cmd_type == Parser.CommandType.A_COMMAND:
                sym = self.parser.symbol(cmd)
                if sym in self.symbol_table:
                    val = self.symbol_table[sym]
                else:
                    val = int(sym)
                codes.append('0' + Code.value(val))
        return '\n'.join(codes)

if __name__ == '__main__':
    import sys
    assembler  = Assembler(sys.argv[1])
    print(assembler.assemble())