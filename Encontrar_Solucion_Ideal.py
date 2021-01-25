"""
En esta clase se busca la mejor solucion
"""

class Encontrar_Solucion_Ideal:

    def __init__(self,Soluciones):
        self.Soluciones = Soluciones
        self.Solucion_ideal = []
        self.Solucion_Mayor_Peso = []
        pass

    def bolsa_Mayor_Precio(self):
        mayor = [0,0,0]
        for i in self.Soluciones:
            #print(i[1])
            if mayor[2] <= i[2]:
                mayor = i

        #print(mayor)
        self.Solucion_ideal = mayor

    def bolsa_mayor_peso(self):
        mayor = [0,0,0]
        for i in self.Solucion_ideal:
            if mayor[1] <=i[1]:
                mayor = i

        self.Solucion_Mayor_Peso = mayor

