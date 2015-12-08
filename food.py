class Food(object):
	def __init__(self, color, origin, recipe):
		self.color = color
		self.origin = origin
		self.recipe = recipe
	def print_recipe(self):
		print self.recipe 

Quesadilla = Food(["white", "cheese color"], "Mexico", "Put butter in pan.\nPlace one tortilla in pan.\nCut cheese and place on top of tortilla in pan.\nCover with second tortilla and heat until cheese melts.\n")
Yogurt_parfait = Food(["white","red","brown"], "USA", "Place yogurt in a bowl.\nCut berries. \nPlace fruit and berries on top of yogurt.\n")
Pasta = Food(["white","red"], "Italy","Bring at least 4 cups water to a boil.\nOnce boiled, add pasta.\nCook for 8 minutes or until done.\nDrain water.\nHeat sauce in side pan.\nPour sauce over pasta and serve.")

Food.print_recipe(Quesadilla)
Food.print_recipe(Yogurt_parfait)
Food.print_recipe(Pasta)


# print Quesadilla.recipe
# print Yogurt_parfait.recipe
# print Pasta.recipe

# print Quesadilla.color
# print Yogurt_parfait.color
# print Pasta.color