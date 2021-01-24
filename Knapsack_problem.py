import copy
from CrearPoblacion import *
from CrearPesos_Precios import *
from CalcularBolsas import *
from Seleccion_Torneo import *
from Hacer_Cruzamiento import *
from Hacer_Mutacion import *
from Encontrar_Solucion_Ideal import *

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
        print("Lista de pesos",self.Pesos)
        print("Lista de precios",self.Precios)
        self.PoblacionNueva = copy.copy(self.PoblacionInicial)



    def buscarSoluacion(self):

        j=0
        while j < self.Num_iteraciones:
            #print("Se esta buscando la solucion...")
            #print("nueva Poblacion:", self.PoblacionNueva)
            listaPesos = []
            listaPrecios = []

            ##funcion Fitnest
            evaluar = CalcularBolsas(self.PoblacionNueva, self.Precios, self.Pesos, self.Capa)
            evaluar.Calcular_PyP_Bolsas()
            #evaluar.obtenerSolucion()
            listaPesos = evaluar.listaPesos
            listaPrecios = evaluar.listaPrecios
            #print(listaPesos)
            #print(listaPrecios)
            #print("Soluciones:",evaluar.ListaSoluciones)
            #if evaluar.ListaSoluciones !=[]:
            #    self.Respuestas.append(evaluar.ListaSoluciones)
            for A, B, C, in zip(self.PoblacionNueva, listaPesos,listaPrecios):
                if B <= self.Capa:
                    self.Respuestas.append([A,B,C])



        # Torneo
            torneo = seleccion_torneo(self.PoblacionNueva, listaPesos)
            torneo.torneo3()
            torneo.mezclar_poblacion()
            poblacionTorneo = torneo.NuevaPoblacion
            #print("poblacion torneo:",poblacionTorneo)
        # Cruzamiento
            cruzamiento = Hacer_cruzamiento(poblacionTorneo, self.Prob_Cruzamiento)
            cruzamiento.cruzarPoblacion2()
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
        solucionID.bolsa_Mayor_Peso()
        print(solucionID.Solucion_ideal)





#prueba1=knapsack(15,4,50,10,20,5,10)
#prueba1.generar_poblacion()
#prueba1.buscarSoluacion()

