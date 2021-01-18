import  random
import math

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
        self.Listaprecios=[]
        self.ListaPesos=[]


    def creaPreciosObjeto(self):
        return random.randint(1,100)


    def crearPrecios(self):
        i=0
        individuo=[]
        while i < self.longitud:
            individuo.append(self.creaPreciosObjeto())
            i=i+1
        self.Listaprecios = individuo
        return self.Listaprecios


    def crearPesosObjetos(self):
        numero = math.floor(self.tama/2)
        return random.randint(0, numero)


    def crearPesos(self):
        i = 0
        individuo = []
        while i < self.longitud:
            individuo.append(self.crearPesosObjetos())
            i = i + 1
        self.ListaPesos = individuo
        return self.ListaPesos



poblacion= CrearPoblacion(15,40)
##poblacion.CrearNuevaPoblacion()
poblacion.crearPrecios()
poblacion.crearPesos()
#print(poblacion.poblacion)
print(poblacion.Listaprecios)
print(poblacion.ListaPesos)

