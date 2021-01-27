import random


''' Esta clase se usa para mutar a los invividuos gen por gen,
    La clase recibe el porcentaje de probabilidad de mutacion
    y el individuo que sera mutado  '''
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


    def muta_o_no(self):
        numero = self.numero_aleatorio()
        if numero <= self.porcentaje:
            return True
        else:
            return False


    # se muta o no al individuo y si es el caso
    def mutar_individuo(self):
        for i in self.ind_ori:
            mutar=self.muta_o_no()
            if mutar == True:
                self.ind_nuevo.append(self.numero_mutado())
            else:
                self.ind_nuevo.append(i)
        return  self.ind_nuevo
