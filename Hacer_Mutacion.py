from Mutacion import *

'''
En esta clase se hace la mutacion de la poblacion, atraves de la clase mutacion 
la cual muta a los individuos uno por uno
'''

class Hacer_Mutacion:

    # al constructor se le pasa la poblacion que sera mutada y la probabilidad de mutacion respectivamente
    def __init__(self,poblacion,probabilidad,rango):
        self.poblacion = poblacion
        self.probabilidad = probabilidad
        self.rango = rango
        self.nuevaPoblacion = []

    def MutarPoblacion(self):
        for i in self.poblacion:
            #se pasa la probabilidad de mutacion y el individuo que sera mutado a la clase Mutacion
            muta = Mutacion(self.probabilidad,i,self.rango)
            self.nuevaPoblacion.append(muta.mutar_individuo())





#B=[[62, 37, 55, 65, 11, 88], [92, 88, 26, 41, 93, 35], [77, 90, 68, 37, 85, 4], [49, 64, 85, 92, 36, 62]]
#poblacionMutada= Hacer_Mutacion(B,70)
#poblacionMutada.MutarPoblacion()
#print(poblacionMutada.nuevaPoblacion)



