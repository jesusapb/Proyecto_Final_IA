import random


''' Esta clase se usa para mutar a los invividuos gen por gen,
    La clase recibe el porcentaje de probabilidad de mutacion y el individuo que sera mutado  '''

class Mutacion:

    # se pasa en el constructor el porcentaje de mutacion y el individuo a mutar
    def __init__(self, porcentaje, ind_ori, rango):
        self.porcentaje = porcentaje
        self.ind_ori = ind_ori
        self.ind_nuevo = []
        self.rango = rango

    def numero_aleatorio(self):
        return random.randint(1, 100)

    def numero_mutado(self):
        return random.randint(0,self.rango)
        #return random.randint(1, 100)


    def muta_o_no(self):
        numero = self.numero_aleatorio()
        if numero <= self.porcentaje:
            #print(numero)
            return True
        else:
            #print(numero)
            return False

    # se muta o no al individuo y si es el caso
    def mutar_individuo(self):
        #print(self.ind_ori)
        #print(self.porcentaje)
        #print(self.ind_ori)
        for i in self.ind_ori:
            #print(i)
            mutar=self.muta_o_no()
            #print(i)
            #print(mutar)
            if mutar == True:
                #print(i)
                #print("si muta")
                #print(mutar)

                ##Aqui se hace la mutacion

                self.ind_nuevo.append(self.numero_mutado())
            else:
                #print(i)
                #print("no muta")
                #print(mutar)
                self.ind_nuevo.append(i)

        return  self.ind_nuevo



#B=[90, 17, 43, 85, 2, 36, 79, 47, 55, 75, 34, 95, 93, 77, 68]
#num=Mutacion(60,B)
#num.mutar_individuo()
#print(num.ind_nuevo)

