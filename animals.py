class Animals(object):
	def __init__(self, name, hasFur, numLegs):
		self.name = name
		self.hasFur = hasFur
		self.numLegs = numLegs
	def hasFur(self):
		if self.hasFur == "yes":
			return True
		else:
			return False
	def numLegs(self):
		if self.numLegs > 2:
			return True
		else:
			return False



Pig = Animals("Charlotte", "no", 4)
Dog = Animals("Rover", "yes" , 4)
Fish = Animals("Nemo", "no", 0)

print Animals.hasFur(Pig)

print Animals.numLegs(Fish)