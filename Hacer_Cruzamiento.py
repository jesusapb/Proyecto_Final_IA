from Cruzamiento import *
from Cruzamiento2 import *
'''
Esta clase se encarga de hacer los cruzamientos de una poblacion
tomando de dos en dos los elementos de una poblacion y haciendo el intercambio de colas
se le debe pasar en el constructor a la poblacion a cruzar y la probabilidad de que hagan este cruzamiento
'''
class Hacer_cruzamiento:
    # se pasa al constructor la poblacion y la probabilidad de cruzamiento
    def __init__(self, poblacion, probabilidad,listaPesos,Capa):
        self.poblacion = poblacion
        self.nuevaPoblacion = []
        self.tama = len(self.poblacion)
        self.probabilidad = probabilidad
        self.listaPesos = listaPesos
        self.Capa = Capa


    #se cruza a la poblacion de dos en dos, por ello la poblacion debe ser par
    def cruzarPoblacion(self):
        i =0
        while i < self.tama:
            A = self.poblacion[i]
            B = self.poblacion[i+1]
            cambio = Cruzamiento(A,B, self.probabilidad)
            cambio.procesoCruzamiento()
            self.nuevaPoblacion.append(cambio.hijoA)
            self.nuevaPoblacion.append(cambio.hijoB)
            i= i + 2


    def cruzarPoblacion2(self):
        i = 0
        while i < self.tama:
            A = self.poblacion[i]
            B = self.poblacion[i + 1]
            cambio = intercambiar2(A,B,self.probabilidad)
            cambio.procesoCruzamiento()
            self.nuevaPoblacion.append(cambio.hijoA)
            self.nuevaPoblacion.append(cambio.hijoB)
            i = i + 2

    def cruzarPoblacion3(self):
        i = 0
        while i < self.tama:
            if (self.listaPesos[i] and self.listaPesos[i+1]) > self.Capa:
                A = self.poblacion[i]
                B = self.poblacion[i + 1]
                cambio = intercambiar2(A, B, self.probabilidad)
                cambio.procesoCruzamiento()
                self.nuevaPoblacion.append(cambio.hijoA)
                self.nuevaPoblacion.append(cambio.hijoB)

            else:
                self.nuevaPoblacion.append(self.poblacion[i])
                self.nuevaPoblacion.append(self.poblacion[i+1])

            i = i + 2


#A=[[62, 37, 55, 41, 93, 35], [92, 88, 26, 65, 11, 88], [77, 90, 68, 37, 36, 62], [49, 64, 85, 92, 85, 4]]
#prueba = Hacer_cruzamiento(A,30)
#prueba.cruzarPoblacion()
#print(prueba.nuevaPoblacion)