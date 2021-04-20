C = 0x01 # carry
Z = 0x02 # zero
I = 0x04 # interrupt disable
D = 0x08 # decimal mode
B = 0x10 # break
V = 0x20 # overflow
N = 0x40 # negative

# Registers
a = 0x00
x = 0x00
y = 0x00
sp = 0x00
pc = 0x0000
status = 0x00

fetched = 0x00

cpu_ram = []

def write(addr, data):
	cpu_ram[addr] = data

def read(addr):
	return cpu_ram[addr]

def fetch():
	global fetched
	fetched = read(pc)

def set_flag(f, v):
	global status
	if v == 0:
		status ^= f
	else:
		status |= f

def get_flag(f):
	if status & f:
		return 1
	else:
		return 0

# ADDRESSING MODES

def IMM():
	pass

def IMP():
	pass

def IND():
	pass

def ABS():
	pass

def ABX():
	pass

def ABY():
	pass

def REL():
	pass

def IZX():
	pass

def IZY():
	pass

def ZP0():
	pass

def ZPX():
	pass

def ZPY():
	pass

# INSTRUCTION

def ADC():
	fetch()
	global a, fetched
	v = a + fetched + get_flag(C)
	
	set_flag(C, int(v > 255))
	set_flag(Z, int(v & 0xFF))
	set_flag(N, v & 0x80)
	
	a = v & 0xFF
	
	return 1

def AND():
	fetch()
	v = a & fetched
	

def BRK():
	pass

for i in range(2048):
	cpu_ram.append(0)
