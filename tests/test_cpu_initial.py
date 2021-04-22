import unittest
from core.nes import cpu

class test_cpu_initial(unittest.TestCase):
	def test_registers(self):
		self.assertEqual(cpu.a, 0x00)
		self.assertEqual(cpu.x, 0x00)
		self.assertEqual(cpu.y, 0x00)
		self.assertEqual(cpu.sp, 0x00)
		self.assertEqual(cpu.pc, 0x0000)
	
	def test_status_flags(self):
		self.assertEqual(cpu.status, 0x00)
	
	def test_variables(self):
		self.assertEqual(cpu.fetched, 0x00)

if __name__ == "__main__":
	unittest.main()
