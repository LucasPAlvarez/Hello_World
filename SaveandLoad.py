import PoblacionIni
import os
import json

#Funcion para guardar la poblacion
def Saving(myPobl):
	with open("Data/savedPob", "wb") as save:
			print("Saving.")
			templine = str(myPobl.generacion) + "\n"
			save.write(templine.encode("utf-8"))
			templine = str(myPobl.probCross) + "\n"
			save.write(templine.encode("utf-8"))
			templine = str(myPobl.probMut) + "\n"
			save.write(templine.encode("utf-8"))
			print("Saving..")
			for gen in myPobl.poblacion:
				templine = (gen.saving()+ " ").encode("utf-8")
				save.write(templine)
			print("Saving Done\n")


#Funcion para cargar los datos de la anterior poblacion
def Loading(cromLenght = 30, pobLength = 10):
	load = open("Data/savedPob", "rb")
	print("Loading.")
	gen = int(load.readline().decode("utf-8"))
	pCross = float(load.readline().decode("utf-8"))
	pMut = float(load.readline().decode("utf-8"))
	tempLineas = load.readlines()
	prevPob = []
	print("Loading..")
	for t in tempLineas:
		temp_list = t.decode("utf-8").split(" ")
		temp_gen = []
		count = {"first" :0, "second": 0}
		for i in temp_list:
			temp_gen.append(int(i))
			count["first"] += 1
			if count["first"] == cromLenght:
				prevPob.append(temp_gen)
				temp_gen = []
				count["first"] = 0
				count["second"] +=1
			if count["second"] == pobLength:
				break
	print("Loading...")		

	load.close()
	print("Loading Done\n")
	return PoblacionIni.PoblacionIni(prevPob, gen, probCross = pCross, probMut = pMut, cantCrom = pobLength)

#Guarda todas las generaciones para poder verlas en un archivo .txt
def saveRecord(texto):
	if not os.path.isfile("Data/pasado.txt"):
		pathFile = open("Data/pasado.txt", "w")
	else:
		pathFile = open("Data/pasado.txt", "a")


	pathFile.write(texto)
	pathFile.write("\n\n")

	pathFile.close()


#Guarda todas las generaciones para poder representarlas en una grafica
def saveHistory(myPobl):
	#Configura algunos valores para guardar
	prome = 0
	mValue = 0
	lValue = 2
	for pob in myPobl.poblacion:
		temp = pob.funcValue()
		if mValue < temp:
			mValue = temp
		if lValue > temp:
			lValue = temp
		prome = prome + temp


	#Si no hay un archivo json, entonces crea datos nuevos
	if not os.path.isfile("Data/data.json"):
		newData ={"minValue":[], "Promedio":[], "maxValue":[]}
		
	else:
		with open("Data/data.json") as jl:
			newData = json.load(jl)

	#Añade los datos nuevos y luego los guarda
	newData["minValue"].append(lValue)
	newData["Promedio"].append(prome/4)
	newData["maxValue"].append(mValue)
	with open("Data/data.json", "w") as sj:
		json.dump(newData, sj)