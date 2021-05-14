def batch_write(addr, arr_data, cpu):
	for i in range(len(arr_data)):
		cpu.write(addr + i, arr_data[i])

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