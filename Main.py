import PoblacionIni
#el main crea una poblacion
myPobl = PoblacionIni.PoblacionIni()
print(myPobl.printAll())


myPobl.makeChildren()
print(myPobl.printAll())
