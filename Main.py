import PoblacionIni
#el main crea una poblacion
myPobl = PoblacionIni.PoblacionIni()
print (myPobl.printAll())

while True: 
	c=input("¿Desea crear otra generación? (S/N)" )
	if c.lower() == "s":
		c=input("ingrese la cantidad de generaciones")
		for i in range(int(c)):
			myPobl.makeChildren()
			print(myPobl.printAll())
	else:
		break