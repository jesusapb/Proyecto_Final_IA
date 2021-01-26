
"""
En esta clase se saca el peso del contenido de cada bolsa en forma individual,
 esta clase es usada por calcularBolsa
"""

class Calculo:

    def __init__(self, listaPesos,listaPrecios,individuo):
        self.listaPesos=listaPesos
        self.listaPrecios = listaPrecios
        self.individuo = individuo
        self.totalPesos = 0
        self.totalPecios= 0

    def CalcularPesoBolsa(self):
        total=0
        for a, b in zip(self.listaPesos, self.individuo):
            pretotal= a *b
            total = total + pretotal
        self.totalPesos = total


    def CalcularPrecioBolsa(self):
        total=0
        for a, b in zip(self.listaPrecios, self.individuo):
            pretotal= a *b
            total = total + pretotal
        self.totalPecios = total


