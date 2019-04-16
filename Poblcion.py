import random
import Cromosoma

class PoblacionIni:
	
	probCross = 0.9
	probMut = 0.001

	def __init__(self):
		self.poblacion = []
		self.generacion = 0
		for i in range(4):
			crom = Cromosoma()				
			self.poblacion.append(crom)

	def __str__(self):
		temp = ""
		for i in self.poblacion:
			for j in i:
				temp += j.__str__()

			temp += "\n"

		return temp

	def __getitem__(self, index):
		return self.poblacion[index]

	def fitness (self, index):
		total = self.totalFitness()
		temp = (self.poblacion[index].funcValue())/total
		return "{:.2}".format(temp)

	def totalFitness (self):
		total = 0
		for i in self.poblacion:
			total += i.funcValue()
		return total

	def ruleta(self):
		x=random.random()
		sum = float(self.fitness(0))
		if x <sum:
			return self.poblacion[0]
		else:
			sum += float(self.fitness(1))
			if x < sum:
				return self.poblacion[1]
			else:
				sum += float(self.fitness(2))
				if x < sum:
					return self.poblacion[2]
				else:
					return self.poblacion[3]

	def father (self):
		self.fathers = []
		for i in range(4):
			self.fathers.append(self.ruleta())

	def crossover(cromosoma1, cromosoma2):
		#devuelve un arreglo con 2 hijos 
		temp = random.randint(0,4)
		cromTemp1 = []
		cromTemp2 = []

		cromTemp1.append(cromosoma1[:temp])
		cromTemp1.append(cromosoma2[temp:])

		cromTemp2.append(cromosoma2[:temp])
		cromTemp2.append(cromosoma1[temp:])

		return[cromTemp1,cromTemp2]

	def makeChildren(self):
		children = []
		for i in range(2):
			x = random.random()
			if x<self.probCross:
				temp = self.crossover(self.fathers[i*2], self.fathers[(i*2)+1])
				children.append(temp[0])
				children.append(temp[1])
			else:
				children.append(self.fathers[i*2])
				children.append(self.fathers[(i*2)+1])

		for c in children:
			x = random.random()
			if x < self.probMut:
				c.mutacion()
		self.poblacion = children
		self.generacion += 1

	def printAll(self):
		#devuelde un string con todos los datos de la generacion de forma ordenada
		pass