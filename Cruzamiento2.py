import random

## se intercambian bit por bit para formar a los hijos, apartir de la probabilidad de intercambio

##se cambiara el nombre a cruzar
class intercambiar2:

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

    #        return random.randint(1,tama-1)

    def prob_Cruzamiento(self):
        # pass
        numero = random.randint(0, 100)
        if numero <= self.probabilidad:
            # print(numero)
            return True
        else:
            # print(numero)
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
                #print("si se edita")
                if A <= B:
                    self.hijoA.append(A)
                    self.hijoB.append(A)
                else:
                    self.hijoA.append(B)
                    self.hijoB.append(B)


            else:
                #print("no se edita")
                self.hijoA.append(A)
                self.hijoB.append(B)



    def construir_hijos2(self):

        pass

    def procesoCruzamiento(self):
        self.hijoA = []
        self.hijoB = []
        # print(self.prob_Cruzamiento())
        if self.prob_Cruzamiento() == True:
            #print("si se cruzaron")
            self.Construir_Hijos()
            self.huboIntercambio=True
        else:
            #print("no se cruzaron")
            self.hijoA = self.ini_A
            self.hijoB = self.ini_B

        # pass

    def resultado_reproduccion(self):
        print("Padres")
        print(self.ini_A)
        print(self.ini_B)
        print("hijos")
        print(self.hijoA)
        print(self.hijoB)
        if self.huboIntercambio == True:
            print("Se intercambio")
        else:
            print("no hubo intercambio")

        print(self.probabilidad)


#A = [1, 1, 0, 1]
#B = [1, 0, 0, 1]

#C = [1, 2, 3, 4, 5, 6]
#D = [0, 1, 6, 5, 2, 1]

#cadena=intercambiar2(C,D,40)
#cadena.procesoCruzamiento()
#cadena.resultado_reproduccion()