from core.nes import cpu
from tests.utils import batch_write
import unittest

class test_batch_write(unittest.TestCase):
	def test_batch_write(self):
		batch_write(0x00, [0x10, 0x20, 0x50, 0x00, 0x01], cpu)
		
		self.assertEqual(cpu.read(0x00), 0x10)
		self.assertEqual(cpu.read(0x01), 0x20)
		self.assertEqual(cpu.read(0x02), 0x50)
		self.assertEqual(cpu.read(0x03), 0x00)
		self.assertEqual(cpu.read(0x04), 0x01)
	
	def test_offset_write(self):
		batch_write(0x10, [0x05, 0x10, 0x30], cpu)
		
		self.assertEqual(cpu.read(0x10), 0x05)
		self.assertEqual(cpu.read(0x11), 0x10)
		self.assertEqual(cpu.read(0x12), 0x30)

if __name__ == "__main__":
	unittest.run()