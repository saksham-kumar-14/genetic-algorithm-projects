import random
from dna import DNA


class Population():
	def __init__(self,target,n):
		self.generations = []
		for i in range(0,n):
			specimen = DNA(target)
			self.generations.append(specimen)


	def getHighestFitness(self):
		ans = self.generations[0]
		for i in self.generations:
			if i.fitness > ans.fitness:
				ans = i
				if i.fitness == 1:
					return i
		return ans

	def select(self):
		selectionArr = []
		for i in self.generations:
			for j in range(0,i.selectionProbability):
				selectionArr.append(i)

		return [random.choice(selectionArr), random.choice(selectionArr)]


###################################################################################

target = ""
while target=="":
	target = input("Type anything...")
target = target.split()

totalGenerations = 1
N = 200
mutationRate = 0.1
result = []
for i in range(len(target)):
	temp = Population(target[i],N)
	result.append(temp)

for i in result:
	temp = 1
	while i.getHighestFitness().fitness != 1:
		for j in range(0,len(i.generations)):
			a,b = i.select()
			child = a.reproduce(b,mutationRate)
			i.generations[j] = child
			temp +=1
		if temp > totalGenerations:
			totalGenerations = temp

print("total tries: ", totalGenerations)
for i in result:
	print(i.getHighestFitness().val)