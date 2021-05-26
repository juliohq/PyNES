def batch_write(addr, data, cpu):
	for i in range(len(data)):
		cpu.write(addr + i, data[i])

def reset_cpu(cpu):
	cpu.a = 0x00
	cpu.x = 0x00
	cpu.y = 0x00
	cpu.sp = 0x00
	cpu.pc = 0x0000
	cpu.status = 0x00

def wait_cpu_clock(cpu):
	while cpu.cycles > 0:
		cpu.clock()