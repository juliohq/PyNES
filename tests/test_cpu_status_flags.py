import unittest
from core.nes import cpu

class cpu_status_flags(unittest.TestCase):
	def test_full_set(self):
		cpu.set_flag(cpu.C, True)
		cpu.set_flag(cpu.Z, 1)
		cpu.set_flag(cpu.I, True)
		cpu.set_flag(cpu.D, 1)
		cpu.set_flag(cpu.B, True)
		cpu.set_flag(cpu.V, 1)
		cpu.set_flag(cpu.N, True)
		self.assertEqual(cpu.status, 127)
	
	def test_no_set(self):
		cpu.set_flag(cpu.C, False)
		cpu.set_flag(cpu.Z, 0)
		cpu.set_flag(cpu.I, False)
		cpu.set_flag(cpu.D, 0)
		cpu.set_flag(cpu.B, False)
		cpu.set_flag(cpu.V, 0)
		cpu.set_flag(cpu.N, False)
		self.assertEqual(cpu.status, 0)
	
	def test_half_set(self):
		cpu.set_flag(cpu.C, True)
		cpu.set_flag(cpu.Z, 0)
		cpu.set_flag(cpu.I, False)
		cpu.set_flag(cpu.D, 1)
		cpu.set_flag(cpu.B, True)
		cpu.set_flag(cpu.V, 0)
		cpu.set_flag(cpu.N, False)
		self.assertEqual(cpu.status, 25)

if __name__ == "__main__":
	unittest.main()
