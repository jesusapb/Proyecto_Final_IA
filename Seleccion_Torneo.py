import random

'''
En esta clase se hace el proceso de seleccion de los mejores individuos que
seran reproducidos, Se pasa al constructor 2 parametros, la poblacion y los
valores Fitnest( el peso de los individuos de la poblacion)
nota: este metodo tiene 3 formas de torneo, la que se usa es la llamada torneo4
'''

class seleccion_torneo:
   # Se pasa añ constructor la poblacion y los valoresFitnest de esta poblacion
    def __init__(self,poblacion,valoresFitnes):
        self.poblacion = poblacion
        self.valoresFitnes = valoresFitnes
        self.tama=len(self.poblacion)
        self.NuevaPoblacion = []


    def torneo(self):
        for i in range(0,self.tama):
            print("Fitnes: ",self.valoresFitnes[i])
            print("El individuo de la poblacion: ",self.poblacion[i])
            num_Ale1= random.randint(0,self.tama)
            num_Ale2 = random.randint(0, self.tama)
            print("numero aleatorio 1:", num_Ale1)
            print("numero aleatorio 2:", num_Ale2)
            if self.valoresFitnes[i] < self.valoresFitnes[num_Ale1]:
                self.NuevaPoblacion.append(self.poblacion[i])
            else:
                self.NuevaPoblacion.append(self.poblacion[num_Ale1])


    # se hace el torneo comparando 2 individuos continuos, se selecciona la mejor, el cual pasa a la nueva poblacion
    def torneo3(self):
        i=0
        while i< self.tama:
            if self.valoresFitnes[(i % self.tama)] < self.valoresFitnes[((i + 1)% self.tama)]:
                self.NuevaPoblacion.append(self.poblacion[(i % self.tama)])
            else:
                self.NuevaPoblacion.append(self.poblacion[(i + 1)% self.tama])
            i = i +1


    #se hace el torneo comparando 3 individuos continuos, se selecciona la mejor
    # (con el fitnest mas bajo), el cual pasa a la nueva poblacion
    def torneo4(self):
        i=0
        while i< self.tama:
            if self.valoresFitnes[(i % self.tama)] < self.valoresFitnes[((i + 1)% self.tama)] and self.valoresFitnes[(i % self.tama)] < self.valoresFitnes[((i + 2)% self.tama)]:
                self.NuevaPoblacion.append(self.poblacion[(i % self.tama)])
            else:
                if self.valoresFitnes[((i + 1) % self.tama)] < self.valoresFitnes[(i % self.tama)] and self.valoresFitnes[((i+ 1) % self.tama)] < self.valoresFitnes[((i + 2) % self.tama)]:
                    self.NuevaPoblacion.append(self.poblacion[(i + 1) % self.tama])
                else:
                    self.NuevaPoblacion.append(self.poblacion[(i + 2) % self.tama])

            i = i + 1

    #se mezcla a la poblacion, para los siguientes pasos
    def mezclar_poblacion(self):
        mezcla = random.sample(self.NuevaPoblacion, self.tama)
        self.NuevaPoblacion = mezcla
