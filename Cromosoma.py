import random
import math

class Cromosoma:

	def __init__(self):
		self.cromosoma = []
		for j in range(5):
			self.cromosoma.append(random.randint(0,1))

	def __iter__(self):
		return iter(self.cromosoma)

	def value(self):
		val = 0
		for i in range(5):
				val += math.pow(2,i) * self.cromosoma[4-i]  
		return int(val)

	def funcValue(self):
		val = math.pow(self.value(), 2)
		return int(val)

	def mutacion (self):
		#muta al azar uno de los digitos del cromosoma
		temp = random.randint(0,4)
		self.cromosoma[temp] = abs(self.cromosoma[temp] - 1)