import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, N, get_flag)
from tests.utils import reset_cpu, wait_cpu_clock

class test_ins_cmp(unittest.TestCase):
	def test_cmp(self):
		reset_cpu(cpu)
		# Make sure the is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0xC9) # CMP (IMM)
		cpu.write(0x01, 0x10) # Parameter
		cpu.a = 0xFF # Initial A register value
		
		cpu.clock()
		
		self.assertEqual(cpu.cycles, 1)
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 1)

if __name__ == "__main__":
	unittest.main()