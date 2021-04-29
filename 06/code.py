def dest(mnemonic):
    if mnemonic == 'M':
        return '001'
    elif mnemonic == 'D':
        return '010'
    elif mnemonic == 'MD':
        return '011'
    elif mnemonic == 'A':
        return '100'
    elif mnemonic == 'AM':
        return '101'
    elif mnemonic == 'AD':
        return '110'
    elif mnemonic == 'AMD':
        return '111'
    else:
        return '000'


def comp(mnemonic):
    m = {
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        'M': '1110000',
        '!D': '0001101',
        '!A': '0110001',
        '!M': '1110001',
        '-D': '0001111',
        '-A': '0110011',
        '-M': '1110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'M+1': '1110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'M-1': '1110010',
        'D+A': '0000010',
        'D+M': '1000010',
        'D-A': '0010011',
        'D-M': '1010011',
        'A-D': '0000111',
        'M-D': '1000111',
        'D&A': '0000000',
        'D&M': '1000000',
        'D|A': '0010101',
        'D|M': '1010101',
    }
    return m[mnemonic]


def jump(mnemonic):
    if mnemonic == 'JGT':
        return '001'
    elif mnemonic == 'JEQ':
        return '010'
    elif mnemonic == 'JGE':
        return '011'
    elif mnemonic == 'JLT':
        return '100'
    elif mnemonic == 'JNE':
        return '101'
    elif mnemonic == 'JLE':
        return '110'
    elif mnemonic == 'JMP':
        return '111'
    else:
        return '000'