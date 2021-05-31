from core.nes import cartridge, cpu
from core.engine import graphics
from math import floor
import pygame

is_debug = True

# pygame.init()
clock = pygame.time.Clock()

clocks = 0

def run():
	if is_debug:
		window = graphics.Window((512, 240))
		debug = graphics.DebugScreen(window.screen)
	else:
		window = graphics.Window((256, 240))
	
	# Game loop
	while True:
		window.draw()
		window.update()
		
		if is_debug:
			global clocks
			if clocks % 3 == 0:
				pygame.display.set_caption("PyNES (FPS: %s | %s)" % (floor(clock.get_fps()), clocks))
			debug.draw()
			clocks += 1
		
		clock.tick(60)
	
	graphics.pygame.quit()
