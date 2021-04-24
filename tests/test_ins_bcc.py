import unittest
from core.nes import cpu
from tests.utils import reset_cpu

class test_ins_bcc(unittest.TestCase):
	def test_bcc(self):
		reset_cpu(cpu)
		
		cpu.write(0x00, 0x10)
		add_cycles = cpu.BCC()
		
		self.assertEqual(cpu.pc, 0x10)
		self.assertEqual(add_cycles, 1)
	
	def test_cross_page(self):
		reset_cpu(cpu)
		
		cpu.write(0x00FF, 0x01)
		cpu.pc = 0x00FF
		add_cycles = cpu.BCC()
		
		self.assertEqual(cpu.pc, 0x0100)
		self.assertEqual(add_cycles, 2)

if __name__ == "__main__":
	unittest.main()
