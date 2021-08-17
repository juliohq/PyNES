import unittest
from core.nes import cpu

class test_cpu_initial(unittest.TestCase):
	def test_registers(self):
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(cpu.x, 0x00)
		self.assertEqual(cpu.y, 0x00)
		self.assertEqual(cpu.sp, 0x00)
		self.assertEqual(cpu.pc, 0x0000)
		self.assertEqual(cpu.status, 0x00)
	
	def test_variables(self):
		self.assertEqual(cpu.fetched, 0x00)
	
	def test_ram(self):
		# RAM size
		self.assertEqual(len(cpu.cpu_ram), 65536)
		
		# RAM access range
		# Accessible
		self.assertEqual(cpu.is_in_range(0x00), True)
		self.assertEqual(cpu.is_in_range(0x10), True)
		self.assertEqual(cpu.is_in_range(0xFF), True)
		self.assertEqual(cpu.is_in_range(0xFFFF), True)
		
		# Out of range
		self.assertEqual(cpu.is_in_range(-0x05), False)
		self.assertEqual(cpu.is_in_range(0x10000), False)

if __name__ == "__main__":
	unittest.main()
