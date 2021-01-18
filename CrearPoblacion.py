import  random
'''  
En esta clase se crea a la poblacion, en base a la logitud y al tamaño que se pasan en el constructor
se regresa a traves del atributo poblacion
'''

class CrearPoblacion:
    # se pasan al constructor la longitud de los individuos y el
    # tamaño de la poblacion respectivamente
    def __init__(self,longitud, tama):
        #longitud de la cadena
        self.longitud= longitud
        #tamaño de la poblacion
        self.tama=tama
        #la poblacio, se crea la lista vacia para facilitar el manejo
        self.poblacion = []

   # se genera una lista de numero del tamaño de la longitud mas uno
    def crearIndivuo(self):
        lista = list(range(1,self.longitud + 1))
        return lista


    def creacromosoma(self):
        return random.randint(1,100)


    def crearIndividuo2(self):
        i=0
        individuo=[]
        while i < self.longitud:
            individuo.append(self.creacromosoma())
            i=i+1
        return individuo

    # se crea el nuevo indivuo al mezclar aleatoriamente una lista del uno al ocho
    # para despues agregarlo a la poblacion
    def CrearNuevaPoblacion(self):
        i=0

        while  i < self.tama:
            ##nuevoIndividuo= random.sample(self.crearIndivuo(),self.longitud)
            nuevoIndividuo= self.crearIndividuo2()
            self.poblacion.append(nuevoIndividuo)
            i = i + 1
        return self.poblacion



poblacion= CrearPoblacion(15,3)
poblacion.CrearNuevaPoblacion()
print(poblacion.poblacion)

