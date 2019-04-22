import PoblacionIni
import os

#funcion para guardar la poblacion
def Saving(myPobl):
	with open("savedPob", "wb") as save:
			print("Saving.")
			templine = str(myPobl.generacion) + "\n"
			save.write(templine.encode("utf-8"))
			print("Saving..")
			for gen in myPobl.poblacion:
				templine = (gen.saving()+ " ").encode("utf-8")
				save.write(templine)
			#save.writelines(x.saving().encode("utf-8") for x in myPobl.poblacion)
			print("Saving Done\n")


#funcion para cargar los datos de la anterior poblacion
def Loading():
	load = open("savedPob", "rb")
	print("Loading.")
	gen = int(load.readline().decode("utf-8"))
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
			if count["first"] == 5:
				prevPob.append(temp_gen)
				temp_gen = []
				count["first"] = 0
				count["second"] +=1
			if count["second"] == 4:
				break
	print("Loading...")		

	load.close()
	print("Loading Done\n")
	return PoblacionIni.PoblacionIni(prevPob, gen)

#guarda todas las generaciones para poder verlas en un archivo .txt
def saveRecord(texto):
	if not os.path.isfile("pasado.txt"):
		pathFile = open("pasado.txt", "w")
	else:
		pathFile = open("pasado.txt", "a")


	pathFile.write(texto)
	pathFile.write("\n\n")

	pathFile.close()


#guarda todas las generaciones para poder representarlas en una frafica
def saveHistory():
	pass