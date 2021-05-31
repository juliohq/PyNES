import pygame
import sys

class Window:
	def __init__(self, size):
		pygame.init()
		
		self.size = size
		
		self.width = self.size[0]
		self.height = self.size[1]
		
		self.black = (0, 0, 0)
		
		self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED)
		pygame.display.set_caption("PyNES")
	
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	
	def draw(self):
		# self.screen.fill(self.black)
		# pygame.display.update()
		pygame.display.flip()

class DebugScreen:
	def __init__(self, surface):
		self.surface = surface
	
	def draw(self):
		surface = pygame.Surface((256, 240))
		pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(0, 0, 256, 240))
		self.surface.blit(surface, (256, 0))