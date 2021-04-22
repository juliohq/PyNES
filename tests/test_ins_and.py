import unittest
from core.nes import cpu
from core.nes.cpu import (Z, N, get_flag)

class test_ins_and(unittest.TestCase):
	def test_true(self):
		cpu.write(0x00, 0xFF)
		cpu.a = 0xFF
		cpu.AND()
		self.assertEqual(cpu.a, 0xFF)
		
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 1)
	
	def test_false(self):
		cpu.write(0x00, 0x00)
		cpu.a = 0x00
		cpu.AND()
		self.assertEqual(cpu.a, 0x00)
		
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(N), 0)
	
	def test_half(self):
		cpu.write(0x00, 0xFF)
		cpu.a = 0x08
		cpu.AND()
		self.assertEqual(cpu.a, 0x08)
		
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(N), 0)

if __name__ == "__main__":
	unittest.main()
