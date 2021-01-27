import copy
from CrearPoblacion import *
from CrearPesos_Precios import *
from CalcularBolsas import *
from Seleccion_Torneo import *
from Hacer_Cruzamiento import *
from Hacer_Mutacion import *
from Encontrar_Solucion_Ideal import *



''' Aqui se desarrolla el algoritmo del problema de la mochila
Al contructor se le pasa la longitud de las cadena,el Tamaño de la poblacion,
la capacidad de la mochila, la probabilidad de mutacion, la probabilidad de
cruzamiento, el numero de iteraciones que va a tener y el rango en que
estaran los genes.'''

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
        self.Pesos = []
        self.Precios = []


    #se crea la poblacion inicial, los pesos y precios
    def generar_poblacion(self):
        poblacion = CrearPoblacion(self.Longitud, self.Tama, self.Rango)
        poblacion.CrearNuevaPoblacion()
        self.PoblacionInicial = poblacion.poblacion
        print("Poblacion inicial: ",self.PoblacionInicial)
        pesosyprecios = CrearPesos_Precios(self.Longitud, self.Capa, self.Rango)
        pesosyprecios.crearPesos()
        self.Pesos = pesosyprecios.ListaPesos
        pesosyprecios.crearPrecios()
        self.Precios = pesosyprecios.Listaprecios
        print("Lista de pesos: ",self.Pesos)
        print("Lista de precios: ",self.Precios)
        self.PoblacionNueva = copy.copy(self.PoblacionInicial)


    ''' Se busca la solucion, evaluando la poblacion, haciendo un torneo
    para encontrar a los mejores individuos, cruzandolos, mutandolos
    y al final encontrar al mejor '''
    def buscarSolucion(self):
        j=0
        while j < self.Num_iteraciones:
            listaPesos = []
            listaPrecios = []
            # se evalua la poblacion en busca de posibles soluciones
            evaluar = CalcularBolsas(self.PoblacionNueva, self.Precios, self.Pesos, self.Capa)
            evaluar.Calcular_PyP_Bolsas()
            listaPesos = evaluar.listaPesos
            #se separa las Respuestas
            listaPrecios = evaluar.listaPrecios
            for A, B, C, in zip(self.PoblacionNueva, listaPesos,listaPrecios):
                if B <= self.Capa:
                    self.Respuestas.append([A,B,C])
        # Torneo
            torneo = seleccion_torneo(self.PoblacionNueva, listaPesos)
            torneo.torneo3()
            torneo.mezclar_poblacion()
            poblacionTorneo = torneo.NuevaPoblacion
        # Cruzamiento
            cruzamiento = Hacer_cruzamiento(poblacionTorneo, self.Prob_Cruzamiento,listaPesos,self.Capa)
            cruzamiento.cruzarPoblacion3()
            poblacionIntercambio = cruzamiento.nuevaPoblacion
        # mutacion
            Mutar = Hacer_Mutacion(poblacionIntercambio, self.Prob_Mutacion,self.Rango)
            Mutar.MutarPoblacion()
            poblacionMutada = Mutar.nuevaPoblacion
            self.PoblacionNueva.clear()
            self.PoblacionNueva = copy.deepcopy(poblacionMutada)

            j = j + 1

        print("soluciones:",self.Respuestas)
        solucionID = Encontrar_Solucion_Ideal(self.Respuestas)
        solucionID.bolsa_Mayor_Precio()
        print("Solucion ideal:",solucionID.Solucion_ideal)
