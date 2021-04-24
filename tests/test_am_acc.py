import unittest
from core.nes import cpu

class test_am_acc(unittest.TestCase):
	def test_acc(self):
		cpu.ACC()
		self.assertEqual(cpu.fetched, cpu.a)
	
	def test_change(self):
		cpu.a == 0x10
		cpu.ACC()
		self.assertEqual(cpu.fetched, cpu.a)

if __name__ == "__main__":
	unittest.main()
