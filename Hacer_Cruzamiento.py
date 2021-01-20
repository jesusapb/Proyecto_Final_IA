from Cruzamiento import *

'''
Esta clase se encarga de hacer los cruzamientos de una poblacion
tomando de dos en dos los elementos de una poblacion y haciendo el intercambio de colas
se le debe pasar en el constructor a la poblacion a cruzar y la probabilidad de que hagan este cruzamiento
'''
class Hacer_cruzamiento:
    # se pasa al constructor la poblacion y la probabilidad de cruzamiento
    def __init__(self, poblacion, probabilidad):
        self.poblacion = poblacion
        self.nuevaPoblacion = []
        self.tama = len(self.poblacion)
        self.probabilidad = probabilidad

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



A=[[62, 37, 55, 41, 93, 35], [92, 88, 26, 65, 11, 88], [77, 90, 68, 37, 36, 62], [49, 64, 85, 92, 85, 4]]
prueba = Hacer_cruzamiento(A,30)
prueba.cruzarPoblacion()
print(prueba.nuevaPoblacion)