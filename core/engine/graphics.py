import pygame

pygame.font.init()
font = pygame.font.SysFont(None, 16)

class Window:
	def __init__(self, size):
		pygame.init()
		
		self.size = size
		
		self.width = self.size[0]
		self.height = self.size[1]
		
		self.black = (0, 0, 0)
		
		self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED)
		pygame.display.set_caption("PyNES")
	
	def draw(self):
		pygame.display.flip()

class Text:
	def __init__(self, surface, font, string, pos=(0, 0)):
		self.surface = surface
		self.font = font
		self.string = string
		self.pos = pos
	
	def draw(self):
		textobj = self.font.render(self.string, 1, (255, 255, 255))
		trect = textobj.get_rect()
		trect.topleft = self.pos
		self.surface.blit(textobj, trect)

class Counter:
	def __init__(self, surface, font, string, pos=(0, 0)):
		self.surface = surface
		self.font = font
		self.string = string
		self.pos = pos
	
	def draw(self):
		textobj = self.font.render(self.string, 1, (255, 255, 255))
		trect = textobj.get_rect()
		trect.topright = self.pos
		self.surface.blit(textobj, trect)

class Debug:
	def __init__(self, screen, cpu=None, renderables=[]):
		self.screen = screen
		self.surface = pygame.Surface((256, 240))
		self.cpu = cpu
		self.cells = []
		self.renderables = renderables
		
		for byte in range(8):
			global font
			self.cells.append(Text(self.surface, font, '', (0, byte * font.get_height())))
	
	def draw(self):
		pygame.draw.rect(self.surface, (0, 0, 255), pygame.Rect(0, 0, 256, 240))
		
		idx = 0
		for cell in self.cells:
			cell.string = "{0:x}".format(self.cpu.read(idx))
			cell.draw()
			idx += 1
		
		for item in self.renderables:
			item.draw()
		
		self.screen.blit(self.surface, (256, 0))