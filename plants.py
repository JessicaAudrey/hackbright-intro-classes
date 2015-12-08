class Plants(object):
	def __init__(self,type_of_plant, is_flowering, seasonal):
		self.type_of_plant = type_of_plant
		self.is_flowering = is_flowering
		self.seasonal = seasonal
	def set_is_flowering(self, is_flowering):
		self.is_flowering = is_flowering
		return is_flowering
	def does_it_come_back(self, seasonal):
		self.seasonal = seasonal
		if seasonal == "perennial":
			print "It sure does!"
		else:
			print "Nope... SUCKER!"

Christmas_Cactus = Plants("cactus", True, "perennial")
Daisy = Plants("flower", False, "seasonal")
Rose = Plants("bush", False, "perennial")

print Rose.set_is_flowering(True)

Daisy.does_it_come_back("seasonal")

