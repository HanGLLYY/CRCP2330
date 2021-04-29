from enum import Enum

class CommandType(Enum):
    A_COMMAND = 1
    C_COMMAND = 2
    L_COMMAND = 3

class Parser:
    def __init__(self, asm):
        self.commands = []
        with open(asm, 'r') as f:
            for line in f:
                line = self.remove_comment(line)
                if line:
                    self.commands.append(line)

    def remove_comment(self, line):
        if '//' in line:
            line = line.split('//', maxsplit=1)[0]
        return line.strip()

    def command_type(self, cmd):
        if cmd.startswith('@'):
            return CommandType.A_COMMAND
        elif cmd.startswith('(') and cmd.endswith(')'):
            return CommandType.L_COMMAND
        else:
            return CommandType.C_COMMAND

    def symbol(self, cmd):
        cmd_type = self.command_type(cmd)
        if cmd_type == CommandType.A_COMMAND:
            return cmd[1:]
        elif cmd_type == CommandType.L_COMMAND:
            return cmd[1:-1]
        else:
            assert False, "symbol should be called only command type is A_COMMAND or L_COMMAND"

    def dest(self, cmd):
        cmd_type = self.command_type(cmd)
        if cmd_type == CommandType.C_COMMAND:
            if '=' in cmd:
                return cmd.split('=', maxsplit=1)[0].strip()
            else:
                return ''
        else:
            assert False, "dest should be called only command type is C_COMMAND"
            
    def comp(self, cmd):
        cmd_type = self.command_type(cmd)
        if cmd_type == CommandType.C_COMMAND:
            if '=' in cmd:
                cmd = cmd.split('=', maxsplit=1)[1].strip()
            if ';' in cmd:
                return cmd.split(';', maxsplit=1)[0].strip()
            else:
                return cmd
        else:
            assert False, "dest should be called only command type is C_COMMAND"

    def jump(self, cmd):
        cmd_type = self.command_type(cmd)
        if cmd_type == CommandType.C_COMMAND:
            if ';' in cmd:
                return cmd.split(';', maxsplit=1)[1].strip()
            else:
                return ''
        else:
            assert False, "jump should be called only command type is C_COMMAND"

if __name__ == '__main__':
    parser = Parser('Add.asm')
    print(parser.commands)
    print(list(CommandType))
    print(parser.command_type('@x'))
    print(parser.command_type('(LOOP)'))
    print(parser.command_type('M=0'))
    print(parser.dest('M=1'))
    print(parser.jump('D;JGT'))