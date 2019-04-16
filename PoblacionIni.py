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

			temp += "\n"

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
		#variables temporales para almacenar otros datos
		strDevolver = ""
		sumaTemp = 0
		maximoTemp = self.poblacion[0]

		# strDevolver almacena todo lo que se va a inprimir
		strDevolver += "generacion {0}\n\n".format(self.generacion)
		strDevolver += "Cromosoma\tValor\tFuncion\tFitness\n"
		strDevolver += "___________________________________________\n"

		for i in self.poblacion:
			strDevolver += "{0}\t\t".format(i)
			strDevolver += "{0}\t".format(i.value())
			strDevolver += "{0}\t".format(i.funcValue())
			#sumaTemp almacena la suma del valor de los cromosomas evaluados en la funcion
			sumaTemp += i.funcValue()
			#maximo guarda el maximo de los cromosomas
			if(maximoTemp.funcValue() < i.funcValue()):
				maximoTemp = i
			strDevolver += "{0}\n".format(self.fitness(i))

		strDevolver += "___________________________________________\n"
		strDevolver += "Suma\t\t{0}\t1\n".format(sumaTemp)
		strDevolver += "Promedio\t\t{0}\t0.25\n".format(sumaTemp/4)
		strDevolver += "Maximo\t\t{0}\t{1}\n".format(maximoTemp.funcValue(), self.fitness(maximoTemp))

		#devuelve el string puede verse en pantalla o guardarse en un .txt
		return strDevolver