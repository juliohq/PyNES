header = {
	"name": 0,        # 4 bytes
	"prg_banks": 0,   # 1 byte
	"chr_banks": 0,   # 1 byte
	"control1": 0,    # 1 byte
	"control2": 0,    # 1 byte
	"tv_system": 0,   # 1 byte
	"tv_system2": 0,  # 1 byte
	"ram_size": 0,    # 1 byte
	"unused": 0,      # 5 bytes
	"file_format": 0,
}

def __init__(self, filename):
	f = open(filename, "rb")
	
	# Load file header
	header["name"] = f.read(4).decode("utf-8")
	header["prg_banks"] = f.read(1)[0]
	header["chr_banks"] = f.read(1)[0]
	header["control1"] = f.read(1)[0]
	header["control2"] = f.read(1)[0]
	header["tv_system"] = f.read(1)[0]
	header["tv_system2"] = f.read(1)[0]
	header["ram_size"] = f.read(1)[0]
	header["unused"] = f.read(5)
	
	# Skip trainer
	if header["control1"] & 0x04:
		f.seek(512)
	
	# Determine file format
	if (header["control1"] >> 2) & 0x02:
		header["file_format"] = 2
	
	# Load PRG data
	for prg in range(header["prg_banks"]):
		pass
	
	# Load CHR data
	for chr in range(header["chr_banks"]):
		pass
	
	f.close()
