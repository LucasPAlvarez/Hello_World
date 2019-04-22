import PoblacionIni
import os
import SaveandLoad as SL
#el main crea una poblacion y es el menu de la misma



# carga la poblacion anterior si existe una, si no crea una nueva al azar
if os.path.isfile("savedPob"):
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


#el Menu empieza aqui
while True: 
	c=input("¿Desea crear otra generación? (S/N)\n" )
	if c.lower() == "s":
		c=input("ingrese la cantidad de generaciones:\n")
		for i in range(int(c)):
			myPobl.makeChildren()
			imprimir = myPobl.printAll()
			print(imprimir)
			SL.saveRecord(imprimir)
	else:
		SL.Saving(myPobl)
		break


