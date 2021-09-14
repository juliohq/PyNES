import re
from core.nes.cpu import lookup
from PyQt5.QtCore import (
    QObject,
    pyqtSignal,
)

class Interpreter(QObject):
    
    mnemonic_lookup = {}
    pyqtSignal()
    
    def __init__(self):
        for ins in lookup:
            self.mnemonic_lookup[ins[0] + ins[2].__name__] = lookup.index(ins)
    
    def read(self, line):
        raw_line = line
        code = []
        
        try:
            line += '\n'
            opcode = re.findall(r'[A-Z]\w+', line)
            if opcode:
                code.append(self.mnemonic_lookup[opcode[0]])
            else:
                print('Invalid opcode')
                return
            
            args = re.findall(r'(?<=\s\$)[0-9a-fA-F]+(?=\n)', line)
            if args:
                for arg in args:
                    code.append(int(arg, 16))
            else:
                print('Invalid arguments')
                return
            
            print(code)
        except KeyError:
            print(f'Parsing error: \'{raw_line}\' is not a valid instruction line')
            
        
        return code
    
    def read_file(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
        
        code = []
        for line in lines:
            self.read(line)
        
        return code