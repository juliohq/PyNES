import unittest
from core.nes import cpu
from core.nes.cpu import (Z, N, get_flag)
from tests.utils import reset_cpu, wait_cpu_clock

class test_ins_and(unittest.TestCase):
	def test_true(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x29) # AND (IMM)
		cpu.write(0x01, 0xFF) # Parameter
		cpu.a = 0xFF
		
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 1) # 2 cycles
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0xFF)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 1)
	
	def test_false(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x29) # AND (IMM)
		cpu.write(0x01, 0xFF) # Parameter
		cpu.a = 0x00
		
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 1) # 2 cycles
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(N), 0)
	
	def test_half(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x29) # AND (IMM)
		cpu.write(0x01, 0xFF) # Parameter
		cpu.a = 0x08
		
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 1) # 2 cycles
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x08)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_zp0(self):
		pass
	
	def test_zpx(self):
		pass
	
	def test_abs(self):
		pass
	
	def test_abx(self):
		pass
	
	def test_aby(self):
		pass
	
	def test_idx(self):
		pass
	
	def test_idy(self):
		pass

if __name__ == "__main__":
	unittest.main()
