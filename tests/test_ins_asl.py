import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, N, get_flag)

class test_ins_asl(unittest.TestCase):
	def test_pattern(self):
		cpu.a = 0xAA
		cpu.ASL()
		self.assertEqual()
	
	def test_odd_pattern(self):
		cpu.a = 0x55
		cpu.ASL()

if __name__ == "__main__":
	unittest.main()
