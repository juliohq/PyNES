import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, V, N, get_flag)
from tests.utils import reset_cpu, wait_cpu_clock

class test_adc(unittest.TestCase):
	def test_simple(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x11)
		
		cpu.a = 0x07
		
		cpu.clock()
		
		self.assertEqual(cpu.cycles, 1)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x18)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_overflow(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x40)
		
		cpu.a = 0x40
		
		cpu.clock()
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x80)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 1)
	
	def test_carry(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x80)
		
		cpu.a = 0x80
		cpu.clock()
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 0)
	
	def test_mul_adc(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x80)
		cpu.write(0x02, 0x69)
		cpu.write(0x03, 0x40)
		cpu.write(0x04, 0x69)
		cpu.write(0x05, 0xFF)
		
		# First
		cpu.a = 0x80
		cpu.clock()
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 0)
		
		# Second
		cpu.clock()
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x41)
		self.assertEqual(cpu.pc, 0x04)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
		
		# Third / negative
		cpu.clock()
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x40)
		self.assertEqual(cpu.pc, 0x06)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_code(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM (three ADC [IMM])
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x10)
		cpu.write(0x02, 0x69)
		cpu.write(0x03, 0x10)
		cpu.write(0x04, 0x69)
		cpu.write(0x05, 0xE0)
		
		# First
		cpu.clock()
		
		self.assertEqual(cpu.cycles, 1)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x10)
		self.assertEqual(cpu.pc, 0x02)
		
		# Second
		cpu.clock()
		
		# Wait CPU clock
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(cpu.pc, 0x04)
		
		# Third
		cpu.clock()
		
		# Wait CPU clock
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(cpu.pc, 0x06)
	
	def test_zp0(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x65) # ADC (Zero Page)
		cpu.write(0x01, 0x20) # Value that points to 0x20 address
		cpu.write(0x20, 0x01) # Value at Page 0x00
		
		cpu.a = 0x10 # Set initial A value
		cpu.clock()  # First clock
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 2)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x11)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_zpx(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x75) # ADC (Zero Page X)
		cpu.write(0x01, 0x80) # Zero Page X
		cpu.write(0x8F, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.x = 0x0F # Initial X register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 3)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(cpu.x, 0x0F)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_zpx_wrap(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x75) # ADC (Zero Page X)
		cpu.write(0x01, 0x80) # Zero Page X
		cpu.write(0x7F, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.x = 0xFF # Initial X register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 3)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(cpu.x, 0xFF)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_abs(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x6D)
		cpu.write(0x01, 0xFF)
		cpu.write(0x02, 0x10)
		cpu.write(0x10FF, 0x10)
		
		cpu.a = 0x10
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 3)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x03)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_abx(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x7D) # ADC (Absolute X)
		cpu.write(0x01, 0x00) # Lo
		cpu.write(0x02, 0x10) # Hi
		cpu.write(0x1001, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.x = 0x01 # Initial X register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 3)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x03)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
		
		# Cross page
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x7D) # ADC (Absolute X)
		cpu.write(0x01, 0xFF) # Lo (0x10FE)
		cpu.write(0x02, 0x10) # Hi (0x10FE)
		cpu.write(0x1100, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.x = 0x01 # Initial X register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 4)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x03)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_aby(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x79) # ADC (Absolute Y)
		cpu.write(0x01, 0x00) # Lo
		cpu.write(0x02, 0x10) # Hi
		cpu.write(0x1001, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.y = 0x01 # Initial Y register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 3)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x03)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
		
		# Cross page
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x79) # ADC (Absolute X)
		cpu.write(0x01, 0xFF) # Lo (0x10FE)
		cpu.write(0x02, 0x10) # Hi (0x10FE)
		cpu.write(0x1100, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.y = 0x01 # Initial X register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 4)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x03)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_izx(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x61) # ADC (Indirect X)
		cpu.write(0x01, 0x20) # Parameter
		cpu.write(0x24, 0x74) # lo
		cpu.write(0x25, 0x20) # hi
		cpu.write(0x2074, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.x = 0x04 # Initial X register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 5)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_izy(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x71) # ADC (Indirect Y)
		cpu.write(0x01, 0x10) # Parameter
		cpu.write(0x10, 0x28) # lo
		cpu.write(0x11, 0x10) # hi
		cpu.write(0x1038, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.y = 0x10 # Initial Y register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 4)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)

		# Cross page
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x71) # ADC (Indirect Y)
		cpu.write(0x01, 0x10) # Parameter
		cpu.write(0x10, 0xFF) # lo
		cpu.write(0x11, 0x10) # hi
		cpu.write(0x110F, 0x10) # Target address
		
		cpu.a = 0x10 # Initial A register value
		cpu.y = 0x10 # Initial Y register value
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 5)
		
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)

if __name__ == "__main__":
	unittest.main()
