from PyQt5.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
)

class CustomCode(QWidget):
	
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)
        self.line = QLineEdit()
        self.line.setPlaceholderText('Enter custom instruction here')
        self.addr_line = QLineEdit()
        self.addr_line.setPlaceholderText('Address (from)')
        self.run = QPushButton('Run')
        
        self.layout.addWidget(self.line, 0, 0, 1, 1)
        self.layout.addWidget(self.addr_line, 0, 1, 1, 1)
        self.layout.addWidget(self.run, 0, 2, 1, 1)
