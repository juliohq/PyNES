import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, N, get_flag)
from tests.utils import reset_cpu, wait_cpu_clock, batch_write

class test_ins_cmp(unittest.TestCase):
	def test_cmp(self):
		reset_cpu(cpu)
		# Make sure the is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		batch_write(0x00, [0xE0, 0x10], cpu)
		# cpu.write(0x00, 0xE0) # CPX (IMM)
		# cpu.write(0x01, 0x10) # Parameter
		cpu.x = 0xFF # Initial X register value
		
		cpu.clock()
		
		self.assertEqual(cpu.cycles, 1) # 2 cycles
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(cpu.pc, 0x02)
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 1)

if __name__ == "__main__":
	unittest.main()