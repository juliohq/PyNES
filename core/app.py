import sys
from core.engine import settings
from core.engine.worker import Worker
from core.engine.interpreter import Interpreter
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
	QMainWindow,
	QApplication,
	QLabel,
	QWidget,
	QVBoxLayout,
)
from core.qt import (
	qtFlags,
	qtInterp,
	qtMemDump,
	qtRegisters,
)

is_debug = settings.config.getboolean('main', 'debug')

# core
thread = QThread()
worker = Worker()

interp = None
if settings.config.getboolean('main', 'interpreter'):
	interp = Interpreter()

# gui
class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('PyNES Debugger')
		self.window = QWidget()
		self.layout = QVBoxLayout(self.window)
		self.setCentralWidget(self.window)
		
		self.show()

app = QApplication([])
ex = App()

# create widgets
engine_clocks = QLabel()
cpu_clocks = QLabel()
fps = QLabel()
instruction = QLabel()
program_counter = QLabel()
registers = qtRegisters.Registers()
flags = qtFlags.Flags()
code = qtInterp.CustomCode(ex.window)
dump = qtMemDump.DumpTable(ex.window, worker)

# add widgets to layout
ex.layout.addWidget(engine_clocks)
ex.layout.addWidget(cpu_clocks)
ex.layout.addWidget(fps)
ex.layout.addWidget(instruction)
ex.layout.addWidget(registers)
ex.layout.addWidget(flags)
ex.layout.addWidget(code)
ex.layout.addWidget(dump)

if '-d' in sys.argv or '--debug' in sys.argv or is_debug:
	print('DEBUG MODE')
	is_debug = True

class interpLine(QObject):
	interpCode = pyqtSignal(int, list) # addr, instruction bytes
	
	def runCode(self):
		custom_code = code.line.text()
		if custom_code:
			machine_code = interp.read(custom_code)
			self.interpCode.emit(0x0000, machine_code)

interp_line = interpLine()
interp_line.interpCode.connect(worker.injectCode)

def update(ec, cc, efps, ins, regs, f):
	engine_clocks.setText(f'Engine Clocks: {ec}')
	cpu_clocks.setText(f'CPU Clocks: {cc}')
	fps.setText(f'FPS: {efps}')
	instruction.setText(f'Current Instruction: {ins}')
	registers.update(regs)
	flags.update(f)

def quit():
	sys.exit()

def run():
	if is_debug:
		# Connect signals
		if interp:
			code.run.pressed.connect(interp_line.runCode)
		
		worker.moveToThread(thread)
		thread.started.connect(worker.run)
		worker.update.connect(update)
		worker.quit.connect(quit)
		thread.start()
		
		app.exec()
	else:
		worker.run()