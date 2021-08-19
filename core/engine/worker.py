import pygame, sys
from pygame.locals import *
from PyQt5.QtCore import QRunnable

class Worker(QRunnable):
	def run(self):
		print("Worker started!")
		
		pygame.init()
		clock = pygame.time.Clock()
		clocks = 0
		paused = False
		screen = pygame.display.set_mode((256, 240))
		
		while True:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_p:
						paused = not paused
					elif event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
				elif event.type == QUIT:
					pygame.quit()
					sys.exit()
			
			if not paused:
				if True:
					clocks += 1
			clock.tick(60)
