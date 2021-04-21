import unittest
from core.nes import cpu

class test_cpu_ram(unittest.TestCase):
	def test_ram_size(self):
		self.assertEqual(len(cpu.cpu_ram), 2048)

if __name__ == "__main__":
	unittest.main()
