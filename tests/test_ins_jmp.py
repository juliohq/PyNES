import unittest
from core.nes import cpu

class test_ins_jmp(unittest.TestCase):
	def test_ins_jmp(self):
		self.assertEqual(cpu.pc, 0x00)
		cpu.write(0x00, 0x800)
		cpu.JMP()
		self.assertEqual(cpu.pc, 0x800)

if __name__ == "__main__":
	unittest.main()
