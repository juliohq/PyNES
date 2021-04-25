import unittest
from core.nes import cpu
from tests.utils import reset_cpu

class test_am_imm(unittest.TestCase):
	def test_imm(self):
		reset_cpu(cpu)
		
		cpu.write(0x00, 0x01)
		cpu.IMM()
		
		self.assertEqual(cpu.fetched, 0x01)
		self.assertEqual(cpu.pc, 0x01)

if __name__ == "__main__":
	unittest.main()
