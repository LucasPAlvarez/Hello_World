import random
import Cromosoma

class PoblacionIni:
	
	probCross = 0.9
	probMut = 0.001

	def __init__(self):
		self.poblacion = []
		self.generacion = 0
		for i in range(4):
			crom = Cromosoma.Cromosoma()				
			self.poblacion.append(crom)

	def __str__(self):
		temp = ""
		for i in self.poblacion:
			for j in i:
				temp += j.__str__()

		return temp

	def __getitem__(self, index):
		return self.poblacion[index]

	#cambie fitness para que pida un cromosoma y no un index
	def fitness (self, crom):
		total = self.totalFitness()
		temp = (crom.funcValue())/total
		return "{:.2}".format(temp)

	def totalFitness (self):
		total = 0
		for i in self.poblacion:
			try:
				total += i.funcValue()
			except:
				print("primer try" + i) 
		return total

	def ruleta(self):
		Arrtemp = [0] *int(float(self.fitness(self.poblacion[0]))* 100) + [1] * int(float(self.fitness(self.poblacion[1]))* 100) + [2] * int(float(self.fitness(self.poblacion[2]))* 100) + [3] * int(float(self.fitness(self.poblacion[3]))* 100)
		
		return random.choice(Arrtemp)

		"""
		x=random.random()
		sum = float(self.fitness(self.poblacion[0]))
		if x <sum:
			return self.poblacion[0]
		else:
			sum += float(self.fitness(self.poblacion[1]))
			if x < sum:
				return self.poblacion[1]
			else:
				sum += float(self.fitness(self.poblacion[2]))
				if x < sum:
					return self.poblacion[2]
				else:
					return self.poblacion[3]
"""
	def father (self):
		self.fathers = []
		for i in range(4):
			self.fathers.append(self.poblacion[self.ruleta()])

	def crossover(self, cromosoma1, cromosoma2):
		#devuelve un arreglo con 2 hijos 
		temp = random.randint(0,4)
		tempCrom = []
		#cromTemp1 = Cromosoma.Cromosoma()
		#cromTemp2 = Cromosoma.Cromosoma()

		#cromosoma1.cromosoma.clear()
		for i in range(5):
			if i <= temp:
				tempCrom.append(cromosoma1[i])
			else:
				tempCrom.append(cromosoma2[i])
		cromTemp1 = Cromosoma.Cromosoma(tempCrom)
		tempCrom.clear()
		#cromosoma2.cromosoma.clear()
		for i in range(5):
			if i <= temp:
				tempCrom.append(cromosoma2[i])
			else:
				tempCrom.append(cromosoma1[i])
		cromTemp2 = Cromosoma.Cromosoma(tempCrom)

		return[cromTemp1,cromTemp2]

	def makeChildren(self):
		children = []
		self.father()
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
		#variables temporales para almacenar otros datos
		strDevolver = ""
		sumaTemp = 0
		maximoTemp = self.poblacion[0]

		# strDevolver almacena todo lo que se va a inprimir
		strDevolver += "generacion {0}\n".format(self.generacion)
		strDevolver += "══════════════\n\n"
		strDevolver += "Cromosoma\tValor\tFuncion\tFitness\n"
		strDevolver += "___________________________________________\n"

		for i in self.poblacion:
			try:
				strDevolver += "{0}\t\t".format(i)
				strDevolver += "{0}\t".format(i.value())
				strDevolver += "{0}\t".format(i.funcValue())
				#sumaTemp almacena la suma del valor de los cromosomas evaluados en la funcion
				sumaTemp += i.funcValue()
				#maximo guarda el maximo de los cromosomas
				if(maximoTemp.funcValue() < i.funcValue()):
					maximoTemp = i
				strDevolver += "{0}\n".format(self.fitness(i))
			except:
				print ("segundo try" + i.__str__())

		strDevolver += "___________________________________________\n"
		strDevolver += "Suma\t\t\t{0}\t1\n".format(sumaTemp)
		strDevolver += "Promedio\t\t{0}\t0.25\n".format(sumaTemp/4)
		strDevolver += "Maximo\t\t\t{0}\t{1}\n".format(maximoTemp.funcValue(), self.fitness(maximoTemp))

		#devuelve el string puede verse en pantalla o guardarse en un .txt
		return strDevolver