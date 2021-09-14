from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QCheckBox,
)

class Flags(QWidget):
    
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        
        self.c_flag = QCheckBox('C')
        self.z_flag = QCheckBox('Z')
        self.i_flag = QCheckBox('I')
        self.d_flag = QCheckBox('D')
        self.b_flag = QCheckBox('B')
        self.v_flag = QCheckBox('V')
        self.n_flag = QCheckBox('N')
        
        self.flags = [
            self.c_flag,
            self.z_flag,
            self.i_flag,
            self.d_flag,
            self.b_flag,
            self.v_flag,
            self.n_flag,
        ]
        
        self.c_flag.setToolTip('Carry')
        self.z_flag.setToolTip('Zero')
        self.i_flag.setToolTip('Interrupt Disable')
        self.d_flag.setToolTip('Decimal Mode')
        self.b_flag.setToolTip('Break')
        self.v_flag.setToolTip('Overflow')
        self.n_flag.setToolTip('Negative')
        
        self.layout.addWidget(self.c_flag)
        self.layout.addWidget(self.z_flag)
        self.layout.addWidget(self.i_flag)
        self.layout.addWidget(self.d_flag)
        self.layout.addWidget(self.b_flag)
        self.layout.addWidget(self.v_flag)
        self.layout.addWidget(self.n_flag)
    
    def update(self, status_flags):
        for i, flag in enumerate(self.flags):
            flag.setChecked(status_flags[i])