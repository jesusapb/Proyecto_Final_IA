from Calculo import *


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
        #Estas impresiones seran opcionales
        #print(self.listaPesos)
        #print(self.listaPrecios)


    def obtenerSolucion(self):
        for A, B,C in zip( self.poblacion,self.listaPesos, self.listaPrecios):
            if B <= self.pesoMochila:
                self.ListaSoluciones.append([A,B,C])

#pesoMochila = 30


#A = [[42, 85, 59, 39], [97, 41, 13, 88], [68, 49, 60, 85], [68, 16, 69, 35]]
#A = [[74, 87, 73, 21, 21, 20, 69, 80, 35, 81, 46, 97, 94, 55, 56], [57, 79, 73, 9, 1, 11, 25, 78, 56, 41, 36, 26, 3, 58, 69],
 #   [19, 12, 78, 28, 10, 2, 49, 13, 16, 42, 66, 94, 53, 76, 53], [53, 73, 22, 95, 1, 38, 15, 14, 3, 29, 19, 25, 38, 21, 18]]
#PE =[1, 2, 2, 14, 14, 1, 3, 15, 17, 18, 25, 15, 5, 23, 12]
#PR =[35, 32, 88, 49, 67, 25, 71, 19, 22, 2, 5, 58, 82, 63, 70]



#NuevaBolsa = CalcularBolsas(A,PR , PE, pesoMochila)
#NuevaBolsa.Calcular_PyP_Bolsas()
#NuevaBolsa.obtenerSolucion()