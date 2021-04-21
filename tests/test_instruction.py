import test
from PyNES import cpu

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
	
	print("C:", cpu.get_flag(cpu.C), "Z:", cpu.get_flag(cpu.Z), "I:", cpu.get_flag(cpu.I), "D:", cpu.get_flag(cpu.D), "B:", cpu.get_flag(cpu.B), "V:", cpu.get_flag(cpu.V), "N:", cpu.get_flag(cpu.N))

# instructions to test (requires reset after each one)

cpu.ADC()
show()
reset()

cpu.AND()
show()
reset()

cpu.ASL()
show()
reset()
