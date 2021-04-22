import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, V, N, get_flag)

class test_adc(unittest.TestCase):
	def test_adc(self):
		cpu.write(0x00, 0x05)
		cpu.a = 0x04
		cpu.ADC()
		
		self.assertEqual(cpu.a, 9)
		self.assertEqual(cpu.pc, 0)
		
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_overflow_adc(self):
		cpu.write(0x00, 0xFF)
		cpu.a = 0xFF
		cpu.ADC()
		
		self.assertEqual(cpu.a, 0xFE)
		self.assertEqual(cpu.pc, 0)
		
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 1)

if __name__ == "__main__":
	unittest.main()
