import  random
import math

''' En esta clase se crean las listas de pesos y precios, en base a la longitud
    de los individuos, la capacidad de los individuos y el rango en que
    pueden estar los precios '''

class CrearPesos_Precios:
    # se pasan al constructor la longitud de los individuos
    #la capcidad de la bolsa y el rango en que estaran los pesos de la lista
    def __init__(self,longitud, capa, rango):
        self.longitud= longitud
        self.capa=capa
        self.Listaprecios=[]
        self.ListaPesos=[]
        self.rango = rango


    def creaPreciosObjeto(self):
        return random.randint(1,self.rango)

    ## Atraves de este metodo se crean los precios de los objetos, estos pueden
    # ir de 1 al limite establecida (En la variable Rango)
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

    # Atraves de este metodo se crean los pesos de los objetos con la condicion:
    # El peso debe estar entre 1 y la mitad de la capacidad de la mochila
    def crearPesos(self):
        i = 0
        individuo = []
        while i < self.longitud:
            individuo.append(self.crearPesosObjetos())
            i = i + 1
        self.ListaPesos = individuo
        return self.ListaPesos
