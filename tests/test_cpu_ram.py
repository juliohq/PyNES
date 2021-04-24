import unittest
from core.nes import cpu

class test_cpu_ram(unittest.TestCase):
	def test_ram_size(self):
		self.assertEqual(len(cpu.cpu_ram), 2048)
	
	def test_ram_range(self):
		self.assertEqual(cpu.is_in_range(0x05), True)
		self.assertEqual(cpu.is_in_range(-0x05), False)
		self.assertEqual(cpu.is_in_range(0x801), False)
		self.assertEqual(cpu.is_in_range(0x7FF), True)
		self.assertEqual(cpu.is_in_range(0x800), False)
		self.assertEqual(cpu.is_in_range(0x00), True)

if __name__ == "__main__":
	unittest.main()
