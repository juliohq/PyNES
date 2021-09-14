import pygame
from pygame.locals import *
from PyQt5.QtCore import pyqtSignal, QObject
from core.nes import cpu

class Worker(QObject):
	update = pyqtSignal(int, int, float, str, list, list)
	clock = pyqtSignal()
	ram_page = pyqtSignal(list)
	quit = pyqtSignal()
	
	clocks = 0
	master_clock = 0
	
	def injectCode(self, addr=0, bytes=[]):
		iaddr = addr
		for byte in bytes:
			cpu.write(addr, byte)
			addr += 1
		cpu.pc = iaddr
		self.paused = False
	
	def read_page(self, idx):
		page = cpu.cpu_ram[idx * 256:idx * 256 + 256]
		self.ram_page.emit(page)
	
	def run(self):
		print('Worker started!')
		
		self.is_running = True
		pygame.init()
		self.clock = pygame.time.Clock()
		self.paused = True
		pygame.display.set_caption('PyNES')
		self.screen = pygame.display.set_mode((256, 240))
		
		while self.is_running:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_p:
						self.paused = not self.paused
					elif event.key == K_ESCAPE:
						self.is_running = False
						self.quit.emit()
						pygame.quit()
				elif event.type == QUIT:
					self.is_running = False
					self.quit.emit()
					pygame.quit()
			
			if not self.is_running:
				break
			
			if self.master_clock % 12 == 0:
				cpu.clock()
			
			if self.master_clock % 350 == 0:
				pygame.display.flip()
				self.clocks += 1
			
			if self.master_clock % 5244 == 0:
				# update
				self.update.emit(
					self.clocks,            # Engine Clocks
					cpu.clock_count,        # CPU Clocks
					self.clock.get_fps(),   # FPS
					cpu.lookup[cpu.op][0], 	# Instruction
					[
						cpu.a,
						cpu.x,
						cpu.y,
						cpu.sp,
						cpu.pc,
					],
					[
						cpu.get_flag(cpu.C),
						cpu.get_flag(cpu.Z),
						cpu.get_flag(cpu.I),
						cpu.get_flag(cpu.D),
						cpu.get_flag(cpu.B),
						cpu.get_flag(cpu.V),
						cpu.get_flag(cpu.N),
					],
				)
			
			self.master_clock += 1
			
			self.clock.tick(10487)