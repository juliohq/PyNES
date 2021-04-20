import pygame
import sys

class Window:
	def __init__(self):
		pygame.init()
		
		self.size = (256, 240)
		
		self.width = self.size[0]
		self.height = self.size[1]
		
		self.black = (0, 0, 0)
		
		self.screen = pygame.display.set_mode(self.size)
	
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
	def draw(self):
		self.screen.fill(self.black)
		pygame.display.flip()

window = Window()

while True:
	window.draw()
	window.update()

pygame.quit()
