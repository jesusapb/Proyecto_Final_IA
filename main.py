from Knapsack_problem import *


if __name__ == "__main__":
    '''se pasa al constructor los siguientes parametros
    Longitud, Tama ,Capa, Prob_Mutacion, Prob_Cruzamiento, Num_iteraciones, Rango =100 '''
    problem=knapsack(15,100, 100,10,40,1000,10)
    problem.generar_poblacion()
    problem.buscarSolucion()




