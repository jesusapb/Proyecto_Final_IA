from Calculo import *

''' En esta clase se calcula el peso de las bolsas que conforman la
    poblacion, hace uso de la clase Calculo para otener en peso de cada bolsa '''

class CalcularBolsas:

    def __init__(self,poblacion,Precios,Pesos, pesoMochila):
        self.poblacion = poblacion
        self.Precios = Precios
        self.Pesos = Pesos
        self.pesoMochila = pesoMochila
        self.listaPesos = []
        self.listaPrecios = []
        self.ListaFitnest=[]
        self.ListaSoluciones = []


    def Calcular_PyP_Bolsas(self):


        for i in self.poblacion:
            CalcularBolsa = Calculo(self.Pesos,self.Precios,i)
            CalcularBolsa.CalcularPesoBolsa()
            CalcularBolsa.CalcularPrecioBolsa()
            self.listaPesos.append(CalcularBolsa.totalPesos)
            self.listaPrecios.append(CalcularBolsa.totalPecios)



    def obtenerSolucion(self):
        for A, B,C in zip( self.poblacion,self.listaPesos, self.listaPrecios):
            if B <= self.pesoMochila:
                self.ListaSoluciones.append([A,B,C])

