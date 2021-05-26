import test

cartridge.load("tests/cpu_dummy_reads.nes")

for prop in cartridge.header:
	print(prop + ":", cartridge.header[prop])
