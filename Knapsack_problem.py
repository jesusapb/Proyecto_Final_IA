import copy
from CrearPoblacion import *
from CrearPesos_Precios import *
from CalcularBolsas import *
from Seleccion_Torneo import *


'''
Aqui se desarrolla el algoritmo del problema de la mochila
'''


class knapsack:

    def __init__(self,Longitud,Tama ,Capa, Prob_Mutacion, Prob_Cruzamiento, Num_iteraciones, Rango =100):
        self.Longitud = Longitud
        #la capacidad de la mochila
        self.Tama = Tama
        self.Capa = Capa
        self.Prob_Mutacion = Prob_Mutacion
        self.Prob_Cruzamiento = Prob_Cruzamiento
        self.Num_iteraciones = Num_iteraciones
        self.Rango= Rango
        self.PoblacionInicial = []
        self.PoblacionNueva = []
        self.Respuestas = []
        self.Pesos = []
        self.Precios = []

    #se crea la poblacion inicial, los pesos y precios

    def generar_poblacion(self):
        poblacion = CrearPoblacion(self.Longitud, self.Tama, self.Rango)
        poblacion.CrearNuevaPoblacion()
        #print(poblacion.poblacion)
        self.PoblacionInicial = poblacion.poblacion
        print(self.PoblacionInicial)
        pesosyprecios = CrearPesos_Precios(self.Longitud, self.Capa, self.Rango)
        pesosyprecios.crearPesos()
        self.Pesos = pesosyprecios.ListaPesos
        pesosyprecios.crearPrecios()
        #print(pesosyprecios.ListaPesos)
        self.Precios = pesosyprecios.Listaprecios
        print(self.Pesos)
        print(self.Precios)
        self.PoblacionNueva = copy.copy(self.PoblacionInicial)

    def buscarSoluacion(self):

        listaPesos = []
        listaPrecios = []
        print("Se esta buscando la solucion...")
        ##funcion Fitnest
        evaluar = CalcularBolsas(self.PoblacionNueva, self.Precios, self.Pesos, self.Capa)
        evaluar.Calcular_PyP_Bolsas()
        listaPesos = evaluar.listaPesos
        listaPrecios = evaluar.listaPrecios
        print(listaPesos)
        print(listaPrecios)


        # Torneo
        torneo = seleccion_torneo(self.PoblacionNueva, listaPesos)
        torneo.torneo4()
        torneo.mezclar_poblacion()
        poblacionTorneo = torneo.NuevaPoblacion
        print(poblacionTorneo)
        # Cruzamiento


        # mutacion





prueba1=knapsack(15,4,50, 50,50,500,10)
prueba1.generar_poblacion()
prueba1.buscarSoluacion()

