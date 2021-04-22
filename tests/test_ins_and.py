import unittest
from core.nes import cpu

class test_ins_and(unittest.TestCase):
	def test_true(self):
		cpu.write(0x00, 0xFF)
		cpu.a = 0xFF
		cpu.AND()
		self.assertEqual(cpu.a, 0xFF)
	
	def test_false(self):
		cpu.write(0x00, 0x00)
		cpu.a = 0x00
		cpu.AND()
		self.assertEqual(cpu.a, 0x00)
	
	def test_half(self):
		cpu.write(0x00, 0xFF)
		cpu.a = 0x08
		cpu.AND()
		self.assertEqual(cpu.a, 0x08)

if __name__ == "__main__":
	unittest.main()
