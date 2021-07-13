from core.engine import graphics, settings
from core.nes import cartridge, cpu
from math import floor
import pygame, sys
from pygame.locals import *

is_debug = settings.config.getboolean('main', 'debug')

paused = False

pygame.init()
clock = pygame.time.Clock()
clocks = 0

def run():
	if is_debug:
		window = graphics.Window((512, 240))
		debug = graphics.Debug(window.screen, cpu)
		
		fps = graphics.Counter(debug.surface, graphics.font, '', (256, 0))
		engine_clocks = graphics.Counter(debug.surface, graphics.font, '', (256, 20))
		cpu_clocks = graphics.Counter(debug.surface, graphics.font, '', (256, 40))
		registers = graphics.Counter(debug.surface, graphics.font, '', (256, 60))
		flags = graphics.Counter(debug.surface, graphics.font, '', (256, 80))
		instruction = graphics.Counter(debug.surface, graphics.font, '', (256, 100))
		
		debug.renderables.extend([fps, engine_clocks, cpu_clocks, registers, flags, instruction])
	else:
		window = graphics.Window((256, 240))
	
	# for x in range(0, 2048, 2):
	# 	cpu.write(x, 0x69)
	# 	cpu.write(x + 1, 0x01)
	
	# Game loop
	while True:
		# cpu.clock()
		
		global paused
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
			elif event.type == VIDEORESIZE and paused:
				window.draw()
		
		if not paused:
			window.draw()
			
			if is_debug:
				fps.string = str(floor(clock.get_fps())) + ' FPS'
				global clocks
				engine_clocks.string = str(clocks) + ' clocks'
				cpu_clocks.string = str(cpu.clock_count) + ' CPU clocks'
				registers.string = 'PC: %s SP: %s A: %s X: %s Y: %s' % (cpu.pc, cpu.sp, cpu.a, cpu.x, cpu.y)
				flags.string = 'C %s Z %s I %s D %s B %s V %s N %s' % (
						cpu.get_flag(cpu.C),
						cpu.get_flag(cpu.Z),
						cpu.get_flag(cpu.I),
						cpu.get_flag(cpu.D),
						cpu.get_flag(cpu.B),
						cpu.get_flag(cpu.V),
						cpu.get_flag(cpu.N),
					)
				instruction.string = 'INS %s' % cpu.lookup[cpu.op][0]
				
				debug.draw()
				
				clocks += 1
		
		clock.tick(60)