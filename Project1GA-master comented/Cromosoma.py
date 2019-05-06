import random
import math

class Cromosoma:

	def __init__(self, data = None, cant = 5):
		#Crea un cromosoma vacio y se insertan 0 y 1 aleatoriamente
		self.cromosoma = []
		if data == None:
			for j in range(cant):
				self.cromosoma.append(random.randint(0,1))
		else:
			self.cromosoma = data

	def __iter__(self):
		#Funcion que permite iterar en el cromosoma
		return iter(self.cromosoma)

	def __str__(self):
		#Funcion que devuelve el contenido del cromosoma como un string
		temp = ""
		for i in self.cromosoma:
			temp += i.__str__()
		return temp

	def __getitem__(self, index):
		#Funcion que devuelve el valor de un cromosoma en el indice
		return self.cromosoma[index]


	def value(self):
		#Convierte el cromosoma en un numero decimal
		val = 0
		for i in range(len(self.cromosoma)):
				try:
					val += math.pow(2,i) * self.cromosoma[(len(self.cromosoma)-1)-i]  
				except:
					print((len(self.cromosoma)-1)-i)
		return int(val)

	def funcValue(self):
		#Devuelve el valor fitness del cromosoma
		val = math.pow(self.value(), 2)
		return int(val)

	def mutacion (self):
		#Muta al azar uno de los digitos del cromosoma
		temp = random.randint(0,len(self.cromosoma)-1)
		self.cromosoma[temp] = abs(self.cromosoma[temp] - 1)

	def saving(self):
		#Guarda un cromosoma
		temp = " ".join(str(x) for x in self.cromosoma)
		return temp
