

class Animal:
	def __init__(self):
		self.num_eyes = 2


	def breathe(self):
		print("Inhale, exhale.")


class Fish(Animal):
	def __init__(self):
		super().__init__()


	def breathe(self):
		super().breathe()
		print("doing this underwater.")


	def swin(self):
		print("moving in water")


peixe_boi = Animal()
tucunare = Fish()

peixe_boi.breathe()
tucunare.breathe()