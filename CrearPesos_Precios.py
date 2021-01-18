import  random
import math

'''  

'''

class CrearPesos_Precios:
    # se pasan al constructor la longitud de los individuos
    #la capcidad de la bolsa
    def __init__(self,longitud, capa):
        #longitud de la cadena
        self.longitud= longitud
        #capacidad de la mochila
        self.capa=capa
        #la poblacio, se crea la lista vacia para facilitar el manejo
        #self.poblacion = []
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
        numero = math.floor(self.capa/2)
        return random.randint(0, numero)


    def crearPesos(self):
        i = 0
        individuo = []
        while i < self.longitud:
            individuo.append(self.crearPesosObjetos())
            i = i + 1
        self.ListaPesos = individuo
        return self.ListaPesos



poblacion= CrearPesos_Precios(15,40)
##poblacion.CrearNuevaPoblacion()
poblacion.crearPrecios()
poblacion.crearPesos()
#print(poblacion.poblacion)
print(poblacion.Listaprecios)
print(poblacion.ListaPesos)

