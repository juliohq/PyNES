import unittest
from core.nes import cpu
from core.nes.cpu import (V, get_flag)
from tests.utils import reset_cpu, wait_cpu_clock

class test_ins_clv(unittest.TestCase):
	def test_clv(self):
		reset_cpu(cpu)
		# Make sure there is no left cycles
		self.assertEqual(cpu.cycles, 0)
		
		# Write code to RAM
		cpu.write(0x00, 0xB8)
		cpu.set_flag(V, 1)
		
		cpu.clock()
		
		self.assertEqual(cpu.cycles, 1) # 2 cycles
		
		# Wait CPU clock
		wait_cpu_clock(cpu)
		
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(cpu.pc, 0x01)

if __name__ == "__main__":
	unittest.main()