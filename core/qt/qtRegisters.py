from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

class Registers(QWidget):
    
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.template = [
            'A: %s',
            'X: %s',
            'Y: %s',
            'SP: %s',
            'PC: %s',
        ]
        
        self.A = QLabel()
        self.X = QLabel()
        self.Y = QLabel()
        self.SP  = QLabel()
        self.PC  = QLabel()
        
        self.A.setToolTip('Accumulator')
        self.X.setToolTip('X')
        self.Y.setToolTip('Y')
        self.SP.setToolTip('Stack Pointer')
        self.PC.setToolTip('Program Counter')
        
        self.layout.addWidget(self.A)
        self.layout.addWidget(self.X)
        self.layout.addWidget(self.Y)
        self.layout.addWidget(self.SP)
        self.layout.addWidget(self.PC)
        
        self.registers = [
            self.A,
            self.X,
            self.Y,
            self.SP,
            self.PC,
        ]
    
    def update(self, regs):
        for i, reg in enumerate(self.registers):
            reg.setText(self.template[i] % regs[i])