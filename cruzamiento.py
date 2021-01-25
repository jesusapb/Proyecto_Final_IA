import random

"""
En esta clase se intercabian las colas apartir de un punto aleatorio, primero se 
considera si se intercambian o no, siguiendo la probabilidad de intercambio
"""
class Cruzamiento:

    def __init__(self, ini_A, ind_B, probabilidad):
        self.ini_A = ini_A
        self.ini_B = ind_B
        self.hijoA = []
        self.hijoB = []
        self.mutoAPartirD = 0
        self.probabilidad = probabilidad

    def imprimirMiembros(self):
        print(self.ini_A)
        print(self.ini_B)
        print(self.hijoA)
        print(self.hijoB)

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
        # pass
        numero = random.randint(0, 100)
        if numero < 50:
            # print(numero)
            return True
        else:
            # print(numero)
            return False

    def Construir_Hijos(self):
        ApartirD = self.numero_aleatorio()
        self.mutoAPartirD = ApartirD
        i = 0
        for A, B in zip(self.ini_A, self.ini_B):
            #print(A)
            #print(B)
            #print("el nivel de bits recorridos es:", i)
            # print(i)
            i = i + 1
            if i > ApartirD:
                #print("se edita")
                #print("el numero aleatorio es:", ApartirD)
                self.hijoA.append(B)
                self.hijoB.append(A)
            else:
                #print("no se edita")
                self.hijoA.append(A)
                self.hijoB.append(B)




    def procesoCruzamiento(self):
        self.hijoA = []
        self.hijoB = []
        # print(self.prob_Cruzamiento())
        if self.prob_Cruzamiento() == True:
            #print("si se cruzaron")
            self.Construir_Hijos()
        else:
            #print("no se cruzaron")
            self.hijoA = self.ini_A
            self.hijoB = self.ini_B



    def resultado_reproduccion(self):
        print("Padres")
        print(self.ini_A)
        print(self.ini_B)
        print("hijos")
        print(self.hijoA)
        print(self.hijoB)
        if self.mutoAPartirD > 0:
            print("Se intercambio a partir de: ")
            print(self.mutoAPartirD)
        else:
            print("no hubo intercambio")

        print(self.probabilidad)




#C = [81, 70, 31, 18, 82, 36, 47, 57, 99, 76, 35, 6, 15, 96, 91]
#D = [73, 62, 53, 80, 49, 16, 19, 77, 51, 27, 53, 15, 68, 40, 17]

#cadena=Cruzamiento(C,D,90)

#print(cadena.numero_aleatorio())
 #cadena.Construir_Hijos()
#cadena.procesoCruzamiento()
#cadena.resultado_reproduccion()
