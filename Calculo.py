

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





#A=[1,2,3,4,5]
#B=[5,4,3,2,1]
#C=[1,2,3,4,5]

#resultado = Calculo(A,B,C)
#resultado.CalcularPesoBolsa()
#resultado.CalcularPrecioBolsa()
#print(resultado.totalPesos)
#print(resultado.totalPecios)

