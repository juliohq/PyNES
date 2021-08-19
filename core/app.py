import sys
from core.engine import settings
from core.engine.worker import Worker
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import QThreadPool

is_debug = settings.config.getboolean('main', 'debug')

paused = False

if '-d' in sys.argv or '--debug' in sys.argv or is_debug:
	print('DEBUG MODE')
	is_debug = True

def run():
	worker = Worker()
	pool = QThreadPool()
	pool.start(worker)
	
	if is_debug:
		app = QApplication([])
		window = QWidget()
		layout = QVBoxLayout()
		window.setLayout(layout)
		layout.addWidget(QPushButton("Button"))
		window.show()
		app.exec()