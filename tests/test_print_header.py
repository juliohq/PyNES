import unittest
from core.nes import cartridge

cartridge.load("tests/cpu_dummy_reads.nes")

for prop in cartridge.header:
	print(prop + ":", cartridge.header[prop])
