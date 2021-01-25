from Knapsack_problem import *



if __name__ == "__main__":
#Longitud, Tama ,Capa, Prob_Mutacion, Prob_Cruzamiento, Num_iteraciones, Rango =100
    prueba1=knapsack(15,100, 100,10,40,1000)
    prueba1.generar_poblacion()
    prueba1.buscarSoluacion()



