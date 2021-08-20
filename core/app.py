import sys
from core.engine import settings
from core.engine.worker import Worker
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QLabel, QPlainTextEdit, QPushButton, QWidget, QVBoxLayout

is_debug = settings.config.getboolean('main', 'debug')

# core
thread = QThread()
worker = Worker()

# gui
app = QApplication([])
window = QWidget()
window.setWindowTitle('PyNES Debugger')
layout = QVBoxLayout()
window.setLayout(layout)

# create widgets
engine_clocks = QLabel()
cpu_clocks = QLabel()
fps = QLabel()
instruction = QLabel()

dump = QPlainTextEdit()
dump.setReadOnly(True)

# add widgets to layout
layout.addWidget(engine_clocks)
layout.addWidget(cpu_clocks)
layout.addWidget(fps)
layout.addWidget(instruction)
layout.addWidget(dump)

if '-d' in sys.argv or '--debug' in sys.argv or is_debug:
	print('DEBUG MODE')
	is_debug = True

def update(ec, cc, efps, ins):
	engine_clocks.setText(f'Engine Clocks: {ec}')
	cpu_clocks.setText(f'CPU Clocks: {cc}')
	fps.setText(f'FPS: {efps}')
	instruction.setText(f'Current Instruction: {ins}')

def quit():
	sys.exit()

def run():
	if is_debug:
		worker.moveToThread(thread)
		thread.started.connect(worker.run)
		worker.update.connect(update)
		worker.quit.connect(quit)
		thread.start()
		
		window.show()
		app.exec()
	else:
		worker.run()