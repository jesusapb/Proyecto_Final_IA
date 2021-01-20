from Calculo import *

class Bolsa:

    def __init__(self,poblacion,Precios,Pesos, pesoMochila):
        self.poblacion = poblacion
        self.Precios = Precios
        self.Pesos = Pesos
        self.pesoMochila = pesoMochila
        self.listaPesos = []
        self.listaPrecios = []


    def CalcularBolsas(self):

        for i in self.poblacion:
            CalcularBolsa = Calculo(self.Pesos,self.Precios,i)
            CalcularBolsa.CalcularPesoBolsa()
            CalcularBolsa.CalcularPrecioBolsa()
            self.listaPesos.append(CalcularBolsa.totalPesos)
            self.listaPrecios.append(CalcularBolsa.totalPecios)

        print(self.listaPesos)
        print(self.listaPrecios)



pesoMochila = 30


#A = [[42, 85, 59, 39], [97, 41, 13, 88], [68, 49, 60, 85], [68, 16, 69, 35]]
A = [[16, 14, 12, 3], [25, 2, 5, 13], [17, 4, 17, 10], [16, 2, 18, 10]]
PE = [21, 25, 2, 9]
PR = [72, 99, 67, 81]


NuevaBolsa = Bolsa(A,PR , PE, pesoMochila)
NuevaBolsa.CalcularBolsas()