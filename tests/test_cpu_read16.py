import unittest
from core.nes import cpu
from tests.utils import reset_cpu

class test_cpu_read16(unittest.TestCase):
	def test_16(self):
		reset_cpu(cpu)
		
		cpu.write(0x00, 0x34)
		cpu.write(0x01, 0x12)
		res = cpu.read_16()
		self.assertEqual(res, 0x1234)
		self.assertEqual(cpu.pc, 0x02)

if __name__ == "__main__":
	unittest.main()
