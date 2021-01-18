import random

## Esta clase se usa para mutar a los invividuos gen por gen

class mutacion:

    def __init__(self, porcentaje, ind_ori):
        self.porcentaje = porcentaje
        self.ind_ori = ind_ori
        self.ind_nuevo = []

    def numero_aleatorio(self):
        return random.randint(1, 100)

    def numero_mutado(self):
        return random.randint(1, 100)


    def muta_o_no(self):
        numero = self.numero_aleatorio()
        if numero <= self.porcentaje:
            #print(numero)
            return True
        else:
            #print(numero)
            return False

    def mutar_individuo(self):
        #print(self.ind_ori)
        #print(self.porcentaje)
        for i in self.ind_ori:
            mutar=self.muta_o_no()
            #print(i)
            #print(mutar)
            if mutar == True:
                #print(i)
                print("si muta")
                #print(mutar)

                ##Aqui se hace la mutacion

                self.ind_nuevo.append(self.numero_mutado())
            else:
                #print(i)
                print("no muta")
                #print(mutar)
                self.ind_nuevo.append(i)

        return  self.ind_nuevo



B=[12,45,65,75,85,22,44,83]
num=mutacion(10,B)
num.mutar_individuo()
print(num.ind_nuevo)

