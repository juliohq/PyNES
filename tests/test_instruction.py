import unittest
from core.nes import cpu

def reset():
	cpu.a = 0x00
	cpu.x = 0x00
	cpu.y = 0x00
	cpu.sp = 0x00
	cpu.pc = 0x0000
	cpu.status = 0x00

def show():
	print("A:", cpu.a)
	print("X:", cpu.x)
	print("Y:", cpu.y)
	print("SP:", cpu.sp)
	print("PC:", cpu.pc)
	
	print("C:", cpu.get_flag(cpu.C))
	print("Z:", cpu.get_flag(cpu.Z))
	print("I:", cpu.get_flag(cpu.I))
	print("D:", cpu.get_flag(cpu.D))
	print("B:", cpu.get_flag(cpu.B))
	print("V:", cpu.get_flag(cpu.V))
	print("N:", cpu.get_flag(cpu.N))

# instructions to test (requires reset after each one)

cpu.ADC()
show()
reset()

# cpu.AND()
# show()
# reset()

# cpu.ASL()
# show()
# reset()
