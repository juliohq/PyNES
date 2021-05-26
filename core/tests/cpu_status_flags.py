import test

def show():
	print("C:", cpu.get_flag(cpu.C))
	print("Z:", cpu.get_flag(cpu.Z))
	print("I:", cpu.get_flag(cpu.I))
	print("D:", cpu.get_flag(cpu.D))
	print("B:", cpu.get_flag(cpu.B))
	print("V:", cpu.get_flag(cpu.V))
	print("N:", cpu.get_flag(cpu.N))

def show_raw():
	print(cpu.status)

show()
cpu.set_flag(cpu.C, True)
cpu.set_flag(cpu.Z, 1)
cpu.set_flag(cpu.I, True)
cpu.set_flag(cpu.D, 1)
cpu.set_flag(cpu.B, True)
cpu.set_flag(cpu.V, 1)
cpu.set_flag(cpu.N, True)
show()
show_raw() # should print 127

cpu.set_flag(cpu.C, False)
cpu.set_flag(cpu.Z, 0)
cpu.set_flag(cpu.I, False)
cpu.set_flag(cpu.D, 0)
cpu.set_flag(cpu.B, False)
cpu.set_flag(cpu.V, 0)
cpu.set_flag(cpu.N, False)
show()
show_raw() # should print 0

cpu.set_flag(cpu.C, True)
cpu.set_flag(cpu.Z, 0)
cpu.set_flag(cpu.I, False)
cpu.set_flag(cpu.D, 1)
cpu.set_flag(cpu.B, True)
cpu.set_flag(cpu.V, 0)
cpu.set_flag(cpu.N, False)
show()
show_raw() # should print 25
