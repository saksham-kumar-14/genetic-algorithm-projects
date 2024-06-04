import random

class DNA():
	def __init__(self, target):
		self.val = ""
		self.target = target
		self.tl = len(target)
		for i in range(0,self.tl):
			self.val += chr(random.randrange(33,126))
		self.fitness = self.getFitness()

		self.selectionProbability = int(self.fitness*100)
		if self.selectionProbability==0:
			self.selectionProbability=1

	def getFitness(self):
		t = 0
		for i in range(0,self.tl):
			if self.val[i] == self.target[i]:
				t += 1
		self.fitness = t/self.tl
		self.fitness = (self.fitness)**6
		return self.fitness

	def reproduce(self,partner,mutationRate):
		mid = self.tl//2
		child = DNA(self.target)
		child.val = self.val[:mid] + partner.val[mid:]
		child.getFitness()
		child.mutate(mutationRate)

		while child.fitness < self.fitness:
			child = DNA(self.target)
			child.val = self.val[:mid] + partner.val[mid:]
			child.getFitness()
			child.mutate(mutationRate)
		return child

	def mutate(self,mutationRate):
		for i in range(0,self.tl):
			if random.random() < mutationRate:
				self.val = self.val[:i] + chr(random.randrange(33,126)) + self.val[i+1:]
				self.getFitness()


