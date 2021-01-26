import  random
'''  
En esta clase se crea a la poblacion, en base a la logitud y al tamaño 
que se pasan en el constructor, ademas del rango en que los genees pueden 
encontrarse se regresa a traves del atributo poblacion
'''

class CrearPoblacion:
    # Se pasan al constructor la longitud de los individuos y el
    # tamaño de la poblacion y el rango en que pueden estar los genes.
    def __init__(self,longitud, tama, rango):
        #longitud de la cadena
        self.longitud= longitud
        #tamaño de la poblacion
        self.tama=tama
        #en rango maximo en que pueden estar los cromosomas
        self.rango = rango
        #la poblacio, se crea la lista vacia para facilitar el manejo
        self.poblacion = []


    def creacromosoma(self):
        #se ajusto a Cero para mejorar el decenso
        return random.randint(0,self.rango)

    # Se genera una lista en base a la longitud  del cromosoma establecida
    def crearIndividuo(self):
        i=0
        individuo=[]
        while i < self.longitud:
            individuo.append(self.creacromosoma())
            i=i+1
        return individuo

    # Se crea una nueva poblacion en base al tamaño establecido
    def CrearNuevaPoblacion(self):
        i=0
        while  i < self.tama:
            nuevoIndividuo= self.crearIndividuo()
            self.poblacion.append(nuevoIndividuo)
            i = i + 1
        return self.poblacion



