from core.nes import cartridge, cpu
from core.engine import graphics

def run():
	window = graphics.Window()
	
	# Game loop
	while True:
		window.draw()
		window.update()
	
	graphics.pygame.quit()
