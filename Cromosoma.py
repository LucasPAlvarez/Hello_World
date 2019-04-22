import random
import math

class Cromosoma:

	def __init__(self, data = None):
		self.cromosoma = []
		if data == None:
			for j in range(5):
				self.cromosoma.append(random.randint(0,1))
		else:
			self.cromosoma = data

	def __iter__(self):
		return iter(self.cromosoma)

	#permite imprimir el cromosoma
	def __str__(self):
		temp = ""
		for i in self.cromosoma:
			temp += i.__str__()
		return temp

	def __getitem__(self, index):
		return self.cromosoma[index]


	def value(self):
		val = 0
		for i in range(5):
				try:
					val += math.pow(2,i) * self.cromosoma[4-i]  
				except:
					print(4-i)
		return int(val)

	def funcValue(self):
		val = math.pow(self.value(), 2)
		return int(val)

	def mutacion (self):
		#muta al azar uno de los digitos del cromosoma
		temp = random.randint(0,4)
		self.cromosoma[temp] = abs(self.cromosoma[temp] - 1)

	def saving(self):
		temp = " ".join(str(x) for x in self.cromosoma)
		return temp