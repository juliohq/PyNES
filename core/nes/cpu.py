# Status flags
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

cpu_ram: list = []

def is_in_range(addr):
	return addr >= 0x00 and addr <= 0x7FF

def write(addr, data):
	if is_in_range(addr):
	cpu_ram[addr] = data

def read(addr):
	if is_in_range(addr):
	return cpu_ram[addr]

def fetch():
	global fetched, pc
	fetched = read(pc)

def set_flag(f, v):
	global status
	if v:
		status |= f
	else:
		status &= ~f

def get_flag(f):
	return int((status & f) == f)

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
	
	sign_a = a & 0x80
	sign_f = fetched & 0x80
	
	set_flag(C, v > 255)
	set_flag(Z, (v & 0xFF) == 0x00)
	set_flag(V, 0)
	if sign_a == sign_f:
		if sign_a == (v & 0x80):
			set_flag(V, 0)
		else:
			set_flag(V, 1)
	set_flag(N, v & 0x80)
	
	a = v & 0xFF
	
	return 1

def AND():
	fetch()
	global a, fetched
	a = a & fetched
	
	set_flag(Z, a == 0)
	set_flag(N, a & 0x80)
	
	return 1
	
def ASL():
	fetch()
	v = fetched << 1
	set_flag(C, a & 0x80)
	set_flag(Z, v == 0x00)
	set_flag(N, (v & 0x80) == 0x80)
	return 0

def BRK():
	pass

def CLV():
	set_flag(V, 0)
	return 2

for i in range(2048):
	cpu_ram.append(0)
