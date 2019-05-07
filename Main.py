import PoblacionIni
import os
import SaveandLoad as SL
import Plotear as plt
#el main crea una poblacion y es el menu de la misma

#crea una carpeta para contener todos losdatos guardados si no existe
if not os.path.exists("Data"):
	os.makedirs("Data")

# carga la poblacion anterior si existe una, si no crea una nueva al azar
if os.path.isfile("Data/savedPob"):
	myPobl = SL.Loading()
	newOne = False

else:
	myPobl = PoblacionIni.PoblacionIni()
	newOne = True
	
imprimir = myPobl.printAll()
print (imprimir)
if newOne:
	print("entro")
	SL.saveRecord(imprimir)
	SL.saveHistory(myPobl)

# funcion que crea nuevas generaciones
def nuevasgeneraciones():
	c = input("ingrese la cantidad de generaciones:\n")
	for i in range(int(c)):
		myPobl.makeChildren()
		imprimir = myPobl.printAll()
		print(imprimir)
		SL.saveRecord(imprimir)
		SL.saveHistory(myPobl)

#funcion para mostrar graficas de barra sobre la generacion
def plotear():
	subject = input("que desea graficar?\n\t1)minValue\n\t2)Promedio\n\t3)MaxValue\n")
	if subject == "1":
		plt.plotear("minValue")
	elif subject == "2":
		plt.plotear("Promedio")
	elif subject == "3":
		plt.plotear("maxValue")


#hace una nueva poblacion y te permite cambiar el crossover y la mutacion
def nuevaGen(myPobl):

	input("se eliminaran los datos de la carpeta Data, copielos y luego precione enter")

	if os.path.isfile("Data/data.json"):
		os.remove("Data/data.json")
	if os.path.isfile("Data/pasado.txt"):
		os.remove("Data/pasado.txt")
	if os.path.isfile("Data/savedPob"):
		os.remove("Data/savedPob")

	newProbCross = float(input("ingrese la probabilidad de Crossover(ingrese 2 si quiere el valor original):\n"))
	newProbMut = float(input("ingrese la probabilidad de Mutacion(ingrese 2 si quiere el valor original):\n"))
	
	if (newProbCross != 2) & (newProbMut != 2):
		print("both 2")
		myPobl = PoblacionIni.PoblacionIni(probCross = newProbCross, probMut = newProbMut)
	elif newProbCross != 2:
		print("Cross 2")
		myPobl = PoblacionIni.PoblacionIni(probCross = newProbCross)
	elif newProbMut != 2:
		print("Mut 2")
		myPobl = PoblacionIni.PoblacionIni(probMut = newProbMut)
	else:
		print("None 2")
		myPobl = PoblacionIni.PoblacionIni()
	
	imprimir = myPobl.printAll()
	print (imprimir)
	SL.saveRecord(imprimir)
	SL.saveHistory(myPobl)
	return myPobl
	



#el Menu empieza aqui
while True: 
	c = input("que desea hacer:\n\n\t1) Generar nuevas genraciones.\n\t2) Plotear\n\t3) Nueva poblacion\n\t4) Salir\n" )
	
	if c == "1":
		nuevasgeneraciones()
	elif c == "2":
		plotear()
	elif c == "3":
		myPobl = nuevaGen(myPobl)
	elif c == "4":
		SL.Saving(myPobl)
		break