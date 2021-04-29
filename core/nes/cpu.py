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

# Helpers
op = 0x00
fetched = 0x00

cycles = 0
clock_count = 0

cpu_ram: list = []

def is_in_range(addr):
	return addr >= 0x00 and addr <= 0xFFFF

# Writes the given data to the given memory address
def write(addr, data):
	if is_in_range(addr):
		cpu_ram[addr] = data

# Reads the content of a given memory address
def read(addr):
	if is_in_range(addr):
		return cpu_ram[addr]

# Reads and returns the next 2 bytes of memory (following little-endian addressing) (a 16-bit address)
def read_16():
	global pc
	lo = read(pc)
	pc += 1
	hi = read(pc)
	pc += 1
	return (hi << 8) | lo

# Reads and returns 2 bytes from the given (following little-endian addressing) (a 16-bit address)
# It doesn't affect program counter register
def read_16_addr(addr):
	lo = read(addr)
	hi = read(addr + 1)
	return (hi << 8) | lo

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
	global fetched, pc
	fetched = read(pc)
	pc += 1
	return 0

def IMP():
	return 0

def ACC():
	global fetched
	fetched = a
	return 0

def IND():
	return 0

def ABS():
	global fetched
	fetched = read(read_16()) # No need to increment pc counter as this already does it
	return 0

def ABX():
	global fetched, pc
	bytes = read_16() # No need to increment pc counter as this already does it
	addr = bytes + x
	fetched = read(addr)
	if (addr & 0xFF00) != (bytes & 0xFF00):
		return 1
	return 0

def ABY():
	global fetched, pc
	bytes = read_16() # No need to increment pc counter as this already does it
	addr = bytes + y
	fetched = read(addr)
	if (addr & 0xFF00) != (bytes & 0xFF00):
		return 1
	return 0

def REL():
	return 0

def IZX():
	global fetched, pc
	bytes = read_16_addr((read(pc) + x) & 0xFF)
	pc += 1
	fetched = read(bytes)
	return 0

def IZY():
	return 0

def ZP0():
	global fetched, pc
	fetched = read(read(pc))
	pc += 1
	return 0

def ZPX():
	global fetched, pc, x
	fetched = read((read(pc) + x) & 0xFF)
	pc += 1
	return 0

def ZPY():
	global fetched, pc, y
	fetched = read((read(pc) + y) & 0xFF)
	pc += 1
	return 0

# INSTRUCTION

def ADC():
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

def BCC():
	global pc
	if get_flag(C) == 0:
		page = pc & 0xFF00
		addr = read(pc)
		pc += addr
		if (pc & 0xFF00) != page:
			return 2
		else:
			return 1
	pc += 1
	return 0

def BCS():
	pass

def BEQ():
	pass

def BIT():
	pass

def BMI():
	pass

def BNE():
	pass

def BPL():
	pass

def BRK():
	pass

def BVC():
	pass

def BVS():
	pass

def CLC():
	set_flag(C, 0)
	return 0

def CLD():
	pass

def CLI():
	set_flag(I, 0)
	return 0

def CLV():
	set_flag(V, 0)
	return 2

def CMP():
	pass

def CPX():
	pass

def CPY():
	pass

def DEC():
	pass

def DEX():
	pass

def DEY():
	pass

def EOR():
	pass

def INC():
	pass

def INX():
	pass

def INY():
	pass

def JMP():
	fetch()
	global pc, fetched
	pc = fetched

def JSR():
	pass

def LDA():
	pass

def LDX():
	pass

def LDY():
	pass

def LSR():
	pass

def NOP():
	pass

def ORA():
	pass

def PHA():
	pass

def PHP():
	pass

def PLA():
	pass

def PLP():
	pass

def ROL():
	pass

def ROR():
	pass

def RTI():
	pass

def RTS():
	pass

def SBC():
	pass

def SEC():
	set_flag(C, 1)
	return 0

def SED():
	pass

def SEI():
	set_flag(I, 1)
	return 0

def STA():
	pass

def STX():
	pass

def STY():
	pass

def TAX():
	pass

def TAY():
	pass

def TSX():
	pass

def TXA():
	pass

def TXS():
	pass

def TYA():
	pass

def XXX():
	pass

# Fill CPU with 16-bit addressable memory
for i in range(0xFFFF):
	cpu_ram.append(0)

lookup = [
	["BRK", BRK, IMP, 7], ["ORA", ORA, IZX, 6], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 3], ["ORA", ORA, ZP0, 3], ["ASL", ASL, ZP0, 5], ["???", XXX, IMP, 5], ["PHP", PHP, IMP, 3], ["ORA", ORA, IMM, 2], ["ASL", ASL, IMP, 2], ["???", XXX, IMP, 2], ["???", NOP, IMP, 4], ["ORA", ORA, ABS, 4], ["ASL", ASL, ABS, 6], ["???", XXX, IMP, 6],
	["BPL", BPL, REL, 2], ["ORA", ORA, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 4], ["ORA", ORA, ZPX, 4], ["ASL", ASL, ZPX, 6], ["???", XXX, IMP, 6], ["CLC", CLC, IMP, 2], ["ORA", ORA, ABY, 4], ["???", NOP, IMP, 2], ["???", XXX, IMP, 7], ["???", NOP, IMP, 4], ["ORA", ORA, ABX, 4], ["ASL", ASL, ABX, 7], ["???", XXX, IMP, 7],
	["JSR", JSR, ABS, 6], ["AND", AND, IZX, 6], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["BIT", BIT, ZP0, 3], ["AND", AND, ZP0, 3], ["ROL", ROL, ZP0, 5], ["???", XXX, IMP, 5], ["PLP", PLP, IMP, 4], ["AND", AND, IMM, 2], ["ROL", ROL, IMP, 2], ["???", XXX, IMP, 2], ["BIT", BIT, ABS, 4], ["AND", AND, ABS, 4], ["ROL", ROL, ABS, 6], ["???", XXX, IMP, 6],
	["BMI", BMI, REL, 2], ["AND", AND, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 4], ["AND", AND, ZPX, 4], ["ROL", ROL, ZPX, 6], ["???", XXX, IMP, 6], ["SEC", SEC, IMP, 2], ["AND", AND, ABY, 4], ["???", NOP, IMP, 2], ["???", XXX, IMP, 7], ["???", NOP, IMP, 4], ["AND", AND, ABX, 4], ["ROL", ROL, ABX, 7], ["???", XXX, IMP, 7],
	["RTI", RTI, IMP, 6], ["EOR", EOR, IZX, 6], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 3], ["EOR", EOR, ZP0, 3], ["LSR", LSR, ZP0, 5], ["???", XXX, IMP, 5], ["PHA", PHA, IMP, 3], ["EOR", EOR, IMM, 2], ["LSR", LSR, IMP, 2], ["???", XXX, IMP, 2], ["JMP", JMP, ABS, 3], ["EOR", EOR, ABS, 4], ["LSR", LSR, ABS, 6], ["???", XXX, IMP, 6],
	["BVC", BVC, REL, 2], ["EOR", EOR, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 4], ["EOR", EOR, ZPX, 4], ["LSR", LSR, ZPX, 6], ["???", XXX, IMP, 6], ["CLI", CLI, IMP, 2], ["EOR", EOR, ABY, 4], ["???", NOP, IMP, 2], ["???", XXX, IMP, 7], ["???", NOP, IMP, 4], ["EOR", EOR, ABX, 4], ["LSR", LSR, ABX, 7], ["???", XXX, IMP, 7],
	["RTS", RTS, IMP, 6], ["ADC", ADC, IZX, 6], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 3], ["ADC", ADC, ZP0, 3], ["ROR", ROR, ZP0, 5], ["???", XXX, IMP, 5], ["PLA", PLA, IMP, 4], ["ADC", ADC, IMM, 2], ["ROR", ROR, IMP, 2], ["???", XXX, IMP, 2], ["JMP", JMP, IND, 5], ["ADC", ADC, ABS, 4], ["ROR", ROR, ABS, 6], ["???", XXX, IMP, 6],
	["BVS", BVS, REL, 2], ["ADC", ADC, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 4], ["ADC", ADC, ZPX, 4], ["ROR", ROR, ZPX, 6], ["???", XXX, IMP, 6], ["SEI", SEI, IMP, 2], ["ADC", ADC, ABY, 4], ["???", NOP, IMP, 2], ["???", XXX, IMP, 7], ["???", NOP, IMP, 4], ["ADC", ADC, ABX, 4], ["ROR", ROR, ABX, 7], ["???", XXX, IMP, 7],
	["???", NOP, IMP, 2], ["STA", STA, IZX, 6], ["???", NOP, IMP, 2], ["???", XXX, IMP, 6], ["STY", STY, ZP0, 3], ["STA", STA, ZP0, 3], ["STX", STX, ZP0, 3], ["???", XXX, IMP, 3], ["DEY", DEY, IMP, 2], ["???", NOP, IMP, 2], ["TXA", TXA, IMP, 2], ["???", XXX, IMP, 2], ["STY", STY, ABS, 4], ["STA", STA, ABS, 4], ["STX", STX, ABS, 4], ["???", XXX, IMP, 4],
	["BCC", BCC, REL, 2], ["STA", STA, IZY, 6], ["???", XXX, IMP, 2], ["???", XXX, IMP, 6], ["STY", STY, ZPX, 4], ["STA", STA, ZPX, 4], ["STX", STX, ZPY, 4], ["???", XXX, IMP, 4], ["TYA", TYA, IMP, 2], ["STA", STA, ABY, 5], ["TXS", TXS, IMP, 2], ["???", XXX, IMP, 5], ["???", NOP, IMP, 5], ["STA", STA, ABX, 5], ["???", XXX, IMP, 5], ["???", XXX, IMP, 5],
	["LDY", LDY, IMM, 2], ["LDA", LDA, IZX, 6], ["LDX", LDX, IMM, 2], ["???", XXX, IMP, 6], ["LDY", LDY, ZP0, 3], ["LDA", LDA, ZP0, 3], ["LDX", LDX, ZP0, 3], ["???", XXX, IMP, 3], ["TAY", TAY, IMP, 2], ["LDA", LDA, IMM, 2], ["TAX", TAX, IMP, 2], ["???", XXX, IMP, 2], ["LDY", LDY, ABS, 4], ["LDA", LDA, ABS, 4], ["LDX", LDX, ABS, 4], ["???", XXX, IMP, 4],
	["BCS", BCS, REL, 2], ["LDA", LDA, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 5], ["LDY", LDY, ZPX, 4], ["LDA", LDA, ZPX, 4], ["LDX", LDX, ZPY, 4], ["???", XXX, IMP, 4], ["CLV", CLV, IMP, 2], ["LDA", LDA, ABY, 4], ["TSX", TSX, IMP, 2], ["???", XXX, IMP, 4], ["LDY", LDY, ABX, 4], ["LDA", LDA, ABX, 4], ["LDX", LDX, ABY, 4], ["???", XXX, IMP, 4],
	["CPY", CPY, IMM, 2], ["CMP", CMP, IZX, 6], ["???", NOP, IMP, 2], ["???", XXX, IMP, 8], ["CPY", CPY, ZP0, 3], ["CMP", CMP, ZP0, 3], ["DEC", DEC, ZP0, 5], ["???", XXX, IMP, 5], ["INY", INY, IMP, 2], ["CMP", CMP, IMM, 2], ["DEX", DEX, IMP, 2], ["???", XXX, IMP, 2], ["CPY", CPY, ABS, 4], ["CMP", CMP, ABS, 4], ["DEC", DEC, ABS, 6], ["???", XXX, IMP, 6],
	["BNE", BNE, REL, 2], ["CMP", CMP, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 4], ["CMP", CMP, ZPX, 4], ["DEC", DEC, ZPX, 6], ["???", XXX, IMP, 6], ["CLD", CLD, IMP, 2], ["CMP", CMP, ABY, 4], ["NOP", NOP, IMP, 2], ["???", XXX, IMP, 7], ["???", NOP, IMP, 4], ["CMP", CMP, ABX, 4], ["DEC", DEC, ABX, 7], ["???", XXX, IMP, 7],
	["CPX", CPX, IMM, 2], ["SBC", SBC, IZX, 6], ["???", NOP, IMP, 2], ["???", XXX, IMP, 8], ["CPX", CPX, ZP0, 3], ["SBC", SBC, ZP0, 3], ["INC", INC, ZP0, 5], ["???", XXX, IMP, 5], ["INX", INX, IMP, 2], ["SBC", SBC, IMM, 2], ["NOP", NOP, IMP, 2], ["???", SBC, IMP, 2], ["CPX", CPX, ABS, 4], ["SBC", SBC, ABS, 4], ["INC", INC, ABS, 6], ["???", XXX, IMP, 6],
	["BEQ", BEQ, REL, 2], ["SBC", SBC, IZY, 5], ["???", XXX, IMP, 2], ["???", XXX, IMP, 8], ["???", NOP, IMP, 4], ["SBC", SBC, ZPX, 4], ["INC", INC, ZPX, 6], ["???", XXX, IMP, 6], ["SED", SED, IMP, 2], ["SBC", SBC, ABY, 4], ["NOP", NOP, IMP, 2], ["???", XXX, IMP, 7], ["???", NOP, IMP, 4], ["SBC", SBC, ABX, 4], ["INC", INC, ABX, 7], ["???", XXX, IMP, 7],
]

def clock():
	global op, pc, cycles, lookup, clock_count
	if cycles == 0:
		op = read(pc) # Read opcode
		pc += 1 # Increment program counter in order to read argument bytes
		
		ins = lookup[op] # Find instruction by opcode
		cycles = ins[3] # Get base cycles
		print(ins[0]) # Print instruction mnemonic
		
		# Run addressing mode to fetch data
		add_cycles = ins[2]()
		
		# Run instruction
		add_cycles += ins[1]()
		
		# Add additional cycles
		cycles += add_cycles
	cycles -= 1
	clock_count += 1
