import test
from PyNES import cpu

def show():
	print("C:", cpu.get_flag(cpu.C), "Z:", cpu.get_flag(cpu.Z), "I:", cpu.get_flag(cpu.I), "D:", cpu.get_flag(cpu.D), "B:", cpu.get_flag(cpu.B), "V:", cpu.get_flag(cpu.V), "N:", cpu.get_flag(cpu.N))

def show_raw():
	print(cpu.status)

show()
cpu.set_flag(cpu.C, 1)
cpu.set_flag(cpu.Z, 1)
cpu.set_flag(cpu.I, 1)
cpu.set_flag(cpu.D, 1)
cpu.set_flag(cpu.B, 1)
cpu.set_flag(cpu.V, 1)
cpu.set_flag(cpu.N, 1)
show()
show_raw() # should print 127

cpu.set_flag(cpu.C, 0)
cpu.set_flag(cpu.Z, 0)
cpu.set_flag(cpu.I, 0)
cpu.set_flag(cpu.D, 0)
cpu.set_flag(cpu.B, 0)
cpu.set_flag(cpu.V, 0)
cpu.set_flag(cpu.N, 0)
show()
show_raw() # should print 0
