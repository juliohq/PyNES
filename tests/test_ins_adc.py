import unittest
from core.nes import cpu
from core.nes.cpu import (C, Z, V, N, get_flag)
from tests.utils import reset_cpu

class test_adc(unittest.TestCase):
	def test_simple(self):
		reset_cpu(cpu)
		
		cpu.write(0x00, 0x11)
		cpu.a = 0x07
		cpu.ADC()
		
		self.assertEqual(cpu.a, 0x18)
		self.assertEqual(cpu.pc, 0)
		
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)
	
	def test_overflow(self):
		reset_cpu(cpu)
		
		cpu.write(0x00, 0x40)
		cpu.a = 0x40
		cpu.ADC()
		
		self.assertEqual(cpu.a, 0x80)
		self.assertEqual(cpu.pc, 0)
		
		self.assertEqual(get_flag(C), 0)
		self.assertEqual(get_flag(Z), 0)
		self.assertEqual(get_flag(V), 1)
		self.assertEqual(get_flag(N), 1)
	
	def test_carry(self):
		reset_cpu(cpu)
		
		cpu.write(0x00, 0x80)
		cpu.a = 0x80
		cpu.ADC()
		
		self.assertEqual(cpu.a, 0)
		self.assertEqual(cpu.pc, 0)
		
		self.assertEqual(get_flag(C), 1)
		self.assertEqual(get_flag(Z), 1)
		self.assertEqual(get_flag(V), 0)
		self.assertEqual(get_flag(N), 0)

if __name__ == "__main__":
	unittest.main()
