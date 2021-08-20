import pygame
from pygame.locals import *
from PyQt5.QtCore import pyqtSignal, QObject
from core.nes import cpu

class Worker(QObject):
	update = pyqtSignal(int, int, float, str)
	clock = pyqtSignal()
	quit = pyqtSignal()
	
	def run(self):
		print('Worker started!')
		
		self.is_running = True
		pygame.init()
		self.clock = pygame.time.Clock()
		self.clocks = 0
		self.paused = False
		pygame.display.set_caption('PyNES')
		self.screen = pygame.display.set_mode((256, 240))
		
		while self.is_running:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_p:
						paused = not paused
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
			
			# update
			self.update.emit(
				self.clocks,            # Engine Clocks
				cpu.clock_count,        # CPU Clocks
				self.clock.get_fps(),   # FPS
				cpu.lookup[cpu.op][0], 	# Instruction
			)
			
			if not self.paused:
				self.clocks += 1
			self.clock.tick(60)
			
			pygame.display.flip()
