import test
from PyNES import cartridge

cart = cartridge.Cartridge("tests/cpu_dummy_reads.nes")

print(cart.header)

for prop in cart.header:
	print(prop + ":", cart.header[prop])
