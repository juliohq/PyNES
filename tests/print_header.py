import test
from PyNES import cartridge

cartridge.load("tests/cpu_dummy_reads.nes")

print(cartridge.header)

for prop in cartridge.header:
	print(prop + ":", cartridge.header[prop])
