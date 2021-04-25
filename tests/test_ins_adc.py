import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, V, N, get_flag)
from tests.utils import reset_cpu

class test_adc(unittest.TestCase):
	def test_simple(self):
		reset_cpu(cpu)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x11)
		
		cpu.a = 0x07
		
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x18)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_overflow(self):
		reset_cpu(cpu)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x40)
		
		cpu.a = 0x40
		
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x80)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 1)
	
	def test_carry(self):
		reset_cpu(cpu)
		
		# Write code to RAM
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x80)
		
		cpu.a = 0x80
		cpu.clock()
		
		self.assertEqual(cpu.a, 0)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 0)
	
	def test_mul_adc(self):
		reset_cpu(cpu)
		
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
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 0)
		
		# Second
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x41)
		self.assertEqual(cpu.pc, 0x04)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
		
		# Third / negative
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x40)
		self.assertEqual(cpu.pc, 0x06)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_code(self):
		reset_cpu(cpu)
		
		# Write code to RAM (three ADC [IMM])
		cpu.write(0x00, 0x69)
		cpu.write(0x01, 0x10)
		cpu.write(0x02, 0x69)
		cpu.write(0x03, 0x10)
		cpu.write(0x04, 0x69)
		cpu.write(0x05, 0xE0)
		
		# First
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x10)
		self.assertEqual(cpu.pc, 0x02)
		
		# Second
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x20)
		self.assertEqual(cpu.pc, 0x04)
		
		# Third
		cpu.clock()
		
		while cpu.cycles > 0:
			cpu.clock()
		
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(cpu.pc, 0x06)

if __name__ == "__main__":
	unittest.main()
