class Todd:
	number_of_fellows = 0

	def __init__(self, fellow=[]):
		if Todd.number_of_fellows < 5:

			self.fellow=fellow 
			Todd.number_of_fellows = Todd.number_of_fellows + 1
		else:
			print("sorry, you can't take anymore fellows")

Todd()
print(Todd.number_of_fellows)
Todd()
print(Todd.number_of_fellows)
Todd()
print(Todd.number_of_fellows)
Todd()
print(Todd.number_of_fellows)
Todd()