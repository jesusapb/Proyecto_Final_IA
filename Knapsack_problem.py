from CrearPoblacion import *
from CrearPesos_Precios import *

'''
Aqui se desarrolla el algoritmo del problema de la mochila
'''


class knapsack:

    def __init__(self,Longitud,Tama ,Capa, Prob_Mutacion, Prob_Cruzamiento, Num_iteraciones, Rango =100):
        self.Longitud = Longitud
        self.Tama = Tama
        self.Capa = Capa
        self.Prob_Mutacion = Prob_Mutacion
        self.Prob_Cruzamiento = Prob_Cruzamiento
        self.Num_iteraciones = Num_iteraciones
        self.Rango= Rango
        self.PoblacionInicial = []
        self.PoblacionNueva = []
        self.Respuestas = []
        self.ListaPesos = []
        self.ListaPrecios = []

    #se crea la poblacion inicial, los pesos y precios

    def generar_poblacion(self):
        poblacion = CrearPoblacion(self.Longitud, self.Tama, self.Rango)
        poblacion.CrearNuevaPoblacion()
        #print(poblacion.poblacion)
        self.PoblacionInicial = poblacion.poblacion
        print(self.PoblacionInicial)
        pesosyprecios = CrearPesos_Precios(self.Longitud, self.Capa, self.Rango)
        pesosyprecios.crearPesos()
        self.ListaPesos = pesosyprecios.ListaPesos
        pesosyprecios.crearPrecios()
        #print(pesosyprecios.ListaPesos)
        self.ListaPrecios = pesosyprecios.Listaprecios
        print(self.ListaPesos)
        print(self.ListaPrecios)





prueba1=knapsack(15,4,10, 50,50,500,10)
prueba1.generar_poblacion()

