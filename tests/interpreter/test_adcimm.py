import unittest
from core.engine import interpreter
from core.nes import cpu
from tests.utils import reset_cpu, wait_cpu_clock

class test_adcimm(unittest.TestCase):
    def test_basic_adcimm(self):
        reset_cpu(cpu)
        
        interp = interpreter.Interpreter(cpu)
        code = interp.read('ADCIMM $10')
        self.assertEqual(code, [105, 0x10])
        
        code = interp.read('ADCIMM $FF')
        self.assertEqual(code, [105, 0xFF])
        
        code = interp.read('ADCIMM $0F')
        self.assertEqual(code, [105, 0x0F])

if __name__ == "__main__":
    unittest.main()