from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTabWidget,
    QPushButton,
)
from PyQt5.QtCore import pyqtSignal

class DumpPage(QWidget):
	read_page = pyqtSignal(int)
	
	def __init__(self, index, parent=None):
		super(QWidget, self).__init__(parent)
		self.layout = QVBoxLayout(self)
		self.label = QLabel()
		self.index = index
		
		self.layout.addWidget(self.label)
	
	def updatePressed(self):
		self.read_page.emit(self.index)
	
	def update(self, ram_page):
		text = ''
		
		for i, byte in enumerate(ram_page):
			text += str(byte) + ' '
			if i % 16 == 15:
				text += '\n'
		
		self.label.setText(text)
		

class DumpTable(QWidget):
	def __init__(self, parent=None, worker=None):
		super(QWidget, self).__init__(parent)
		self.layout = QVBoxLayout(self)
		
		# Set up tabs
		self.tablist = []
		self.tabs = QTabWidget()
		for i in range(256):
			tab = DumpPage(i)
			self.tablist.append(tab)
			
			button = QPushButton(f'Update page {tab.index}')
			tab.layout.addWidget(button)
			button.clicked.connect(tab.updatePressed)
			tab.read_page.connect(worker.read_page)
			worker.ram_page.connect(tab.update)
		
		self.tabs.setMinimumSize(350, 350)
		
		# Add tabs
		for i, tab in enumerate(self.tablist):
			self.tabs.addTab(tab, f'Page {i}')
		
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)