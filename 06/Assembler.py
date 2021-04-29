import code
import Parser
import Code

class Assembler:
    def __init__(self, asm):
        self.parser = Parser.Parser(asm)
        self.symbol_table = {}

    def assemble(self):
        codes = []
        for cmd in self.parser.commands:
            cmd_type = self.parser.command_type(cmd)
            if cmd_type == Parser.CommandType.A_COMMAND:
                pass
            elif cmd_type == Parser.CommandType.C_COMMAND:
                dest = Code.dest(self.parser.dest(cmd))
                comp = Code.comp(self.parser.comp(cmd))
                jump = Code.jump(self.parser.jump(cmd))
                codes.append('111' + comp + dest + jump)
        print(codes)

if __name__ == '__main__':
    assembler  = Assembler('Add.asm')
    assembler.assemble()
    
