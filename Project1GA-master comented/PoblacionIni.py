import random
import Cromosoma

class PoblacionIni:
	
	def __init__(self, prevPob = [], gen = 0, probCross = 0.9, probMut = 0.001, cantCrom = 4):
		#funcion que define todas las constantes implicadas en el ejercicio
		#se generan los primeros cromosomas indicado		
		self.poblacion = []
		self.generacion = gen
		self.probCross = probCross
		self.probMut = probMut
		if prevPob == []:
			for i in range(cantCrom):
				crom = Cromosoma.Cromosoma()				
				self.poblacion.append(crom)
		else:
			for data in prevPob:
				self.poblacion.append(Cromosoma.Cromosoma(data))
			


	def __str__(self):
		#el iluminado que lea esto digame que es, flashee y no lo recuerdo
		temp = ""
		for i in self.poblacion:
			for j in i:
				temp += j.__str__()

		return temp

	def __getitem__(self, index):
		#devuelve un objeto de la poblacion indicado por el indice
		return self.poblacion[index]

	def fitness (self, crom):
		#calcula el fitness de cada cromosoma
		total = self.totalFitness()
		temp = (crom.funcValue())/total
		return "{:.2}".format(temp)

	def totalFitness (self):
		#calcula el fitness total de la suma de todos los cromosomas
		total = 0
		for i in self.poblacion:
			try:
				total += i.funcValue()
			except:
				print("primer try" + i) 
		return total

	def ruleta(self):
		Arrtemp = []
		for i in range(len(self.poblacion)):
			Arrtemp += [i] *int(float(self.fitness(self.poblacion[i]))* 100)		
		return random.choice(Arrtemp)

	def father (self):
		#se guardan los padres generados en la ruleta
		self.fathers = []
		for i in range(len(self.poblacion)):
			self.fathers.append(self.poblacion[self.ruleta()])

	def crossover(self, cromosoma1, cromosoma2):
		#devuelve 2  cromosomas hijos 
		temp = random.randint(0,len(cromosoma2.cromosoma)-1)
		tempCrom = []
		for i in range(len(cromosoma2.cromosoma)):
			if i <= temp:
				tempCrom.append(cromosoma1[i])
			else:
				tempCrom.append(cromosoma2[i])
		cromTemp1 = Cromosoma.Cromosoma(tempCrom, len(cromosoma2.cromosoma))
		tempCrom.clear()
		for i in range(len(cromosoma2.cromosoma)):
			if i <= temp:
				tempCrom.append(cromosoma2[i])
			else:
				tempCrom.append(cromosoma1[i])
		cromTemp2 = Cromosoma.Cromosoma(tempCrom)

		return[cromTemp1,cromTemp2]

	def makeChildren(self):
		#funcion en la que se crean los hijos en base al crossover o mutacion
		children = []
		self.father()
		for i in range(len(self.poblacion)//2):
			x = random.random()
			if x<self.probCross:
				temp = self.crossover(self.fathers[i*2], self.fathers[(i*2)+1])
				children.append(temp[0])
				children.append(temp[1])
			else:
				children.append(self.fathers[i*2])
				children.append(self.fathers[(i*2)+1])

		# en el caso de que la poblacion sea impar
		if len(self.poblacion)%2 == 1:
			temp = self.crossover(self.fathers[len(self.fathers)-1], self.fathers[0])
			children.append(temp[0])

		for c in children:
			x = random.random()
			if x < self.probMut:
				c.mutacion()
		self.poblacion = children
		self.generacion += 1

	def printAll(self):
		#devuelve un string con todos los datos de la generacion de forma ordenada
		#variables temporales para almacenar otros datos
		strDevolver = ""
		sumaTemp = 0
		maximoTemp = self.poblacion[0]

		# strDevolver almacena todo lo que se va a inprimir
		strDevolver += "generacion {0}\n".format(self.generacion)
		strDevolver += "---------------\n\n"
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