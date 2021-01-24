import  random
import math

'''  

'''

class CrearPesos_Precios:
    # se pasan al constructor la longitud de los individuos
    #la capcidad de la bolsa
    def __init__(self,longitud, capa, rango):
        #longitud de la cadena
        self.longitud= longitud
        #capacidad de la mochila
        self.capa=capa
        #la poblacio, se crea la lista vacia para facilitar el manejo
        self.Listaprecios=[]
        self.ListaPesos=[]
        self.rango = rango


    def creaPreciosObjeto(self):
        return random.randint(1,self.rango)
        #return random.randint(1,100)


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
        return random.randint(1, numero)


    def crearPesos(self):
        i = 0
        individuo = []
        while i < self.longitud:
            individuo.append(self.crearPesosObjetos())
            i = i + 1
        self.ListaPesos = individuo
        return self.ListaPesos



#poblacion= CrearPesos_Precios(15,50,100)
#poblacion.crearPrecios()
#poblacion.crearPesos()
#print(poblacion.ListaPesos)
#print(poblacion.Listaprecios)
