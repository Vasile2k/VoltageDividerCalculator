
values = [100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910]

vIn  = float(input("Input  voltage: "))
vOut = float(input("Output voltage: "))

delta = float(input("Approximation(%): "))/100.0

class VoltageDivider():

	"""Voltage Divider"""
	r1   = 0
	r2   = 0
	vOut = 0

	def __init__(self, r1, r2, vOut):
		self.r1 = r1
		self.r2 = r2
		self.vOut = vOut

	def __str__(self):
		return "R1: " + str(self.r1) + "    R2: " + str(self.r2) + "    Vout: " + str(self.vOut)

	pass

goodValues = []

for r1 in values:
	for r2 in values:
		output = vIn * r2 / (r1 + r2)
		if abs(vOut - output) <= delta*vOut:
			div = VoltageDivider(r1, r2, output)
			goodValues.append(div)


for divider in goodValues:
	print divider