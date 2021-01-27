import random


''' Apartir de la probabilidad de intercambio se determina si cruzan o no
dos individuos, se sortea si el indivuos intercambian genes y cuando lo
hacen se replica el gen de menor peso'''
class Cruzamiento2:
    #se le pasan al contructor los dos indivuos y la probabilidad de intercambio
    def __init__(self, ini_A, ind_B, probabilidad):
        self.ini_A = ini_A
        self.ini_B = ind_B
        self.hijoA = []
        self.hijoB = []
        self.huboIntercambio = False
        self.probabilidad = probabilidad


    def numero_aleatorio(self):
        tama = len(self.ini_A)
        return random.randint(0, tama)


    def prob_Cruzamiento(self):
        numero = random.randint(0, 100)
        if numero <= self.probabilidad:
            return True
        else:
            return False


    def NuevaProbabilidad(self):
        numero = random.randint(0, 100)
        if numero < 50:
            return True
        else:
            return False

    def Construir_Hijos(self):
        for A,B in zip(self.ini_A,self.ini_B):
            seIntercambia=self.NuevaProbabilidad()
            if seIntercambia == True:
                if A <= B:
                    self.hijoA.append(A)
                    self.hijoB.append(A)
                else:
                    self.hijoA.append(B)
                    self.hijoB.append(B)
            else:
                self.hijoA.append(A)
                self.hijoB.append(B)


    def procesoCruzamiento(self):
        self.hijoA = []
        self.hijoB = []
        if self.prob_Cruzamiento() == True:
            self.Construir_Hijos()
            self.huboIntercambio=True
        else:
            self.hijoA = self.ini_A
            self.hijoB = self.ini_B
