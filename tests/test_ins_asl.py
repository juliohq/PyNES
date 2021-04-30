import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, N, get_flag)
from tests.utils import reset_cpu, wait_cpu_clock

class test_ins_asl(unittest.TestCase):
	def test_pattern(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x0A) # ASL (ACC)
		cpu.a = 0xAA # Initial A register value
		
		cpu.clock()
		
		# Make sure cycle count is correct
		self.assertEqual(cpu.cycles, 2)
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0x54)
		self.assertEqual(cpu.pc, 0x01)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_odd_pattern(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0x0A)
		cpu.a = 0x55
		
		cpu.clock()
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.a, 0xAA)
		self.assertEqual(cpu.pc, 0x01)
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 1)

if __name__ == "__main__":
	unittest.main()
