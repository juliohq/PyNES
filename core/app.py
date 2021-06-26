from core.engine import settings
from .nes import cartridge, cpu
from .engine import graphics
from math import floor
import pygame, sys
from pygame.locals import *

is_debug = True

paused = False

# pygame.init()
clock = pygame.time.Clock()
clocks = 0

def run():
	if is_debug:
		window = graphics.Window((512, 240))
		debug = graphics.DebugScreen(window.screen, None)
		fps = graphics.Counter(debug.surface, graphics.font, '', (256, 0))
		engine_clocks = graphics.Counter(debug.surface, graphics.font, '', (256, 20))
		cpu_clocks = graphics.Counter(debug.surface, graphics.font, '', (256, 40))
		debug.renderables.extend([fps, engine_clocks, cpu_clocks])
	else:
		window = graphics.Window((256, 240))
	
	# Game loop
	while True:
		global paused
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_p:
					paused = not paused
			elif event.type == QUIT:
				sys.exit()
			elif event.type == VIDEORESIZE and paused:
				window.draw()
		
		if not paused:
			window.draw()
			
			if is_debug:
				fps.string = str(floor(clock.get_fps())) + ' FPS'
				global clocks
				engine_clocks.string = str(clocks) + ' clocks'
				cpu_clocks.string = str(cpu.clock_count) + ' CPU clocks'
				debug.draw()
				
				clocks += 1
		
		clock.tick(60)
