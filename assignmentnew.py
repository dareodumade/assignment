class Todd:
	number_of_fellows = 0

	def __init__(self, fellow=[]):
		if Todd.number_of_fellows < 4:

			self.fellow=fellow 
			Todd.number_of_fellows = Todd.number_of_fellows + 1
		else:
			print("sorry, we can't afford to hire anymore fellows")


Todd()
print("Pascal, DRC {}".format(Todd.number_of_fellows))
Todd() 
print("Andrew, USA{}".format(Todd.number_of_fellows))
Todd()
print("Miishe, GH/Murika {}".format(Todd.number_of_fellows))
Todd()
print("Simphiwe, Africa Sur {}".format(Todd.number_of_fellows))
Todd()
print(Todd.number_of_fellows)