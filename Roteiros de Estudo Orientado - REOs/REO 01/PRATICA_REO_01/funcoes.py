########################################################################################################################
# DATA: 02/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro
########################################################################################################################
# TEMA: Funções
########################################################################################################################
#Exemplo 02: Função para amostrar valores de um vetor e calcular sua média
import numpy as np
import random

def amostrar(vetor,tamanho_amostra = None,numero_amostragens = 100):
    vetor = list(vetor)
    if tamanho_amostra == None:
        tamanho_amostra = len(vetor)
    else:
        tamanho_amostra = tamanho_amostra

    print('Vetor: ' +str(vetor))
    print('Tamanho da Amostra: ' + str(tamanho_amostra))

    somador = 0
    it = 0
    matriz_resultado = np.zeros((numero_amostragens,6))
    for i in np.arange(0,numero_amostragens,1):
        it += 1  # it = it+1
        print('Amostragem: ' + str(it))
        print('Vetor: ' + str(vetor))
        print('Tamanho da Amostra: ' + str(tamanho_amostra))

        matriz_resultado[i,0] = it

        amostra = random.sample(vetor, tamanho_amostra)
        print('Amostra: ' + str(amostra))

        media = np.mean(amostra)
        matriz_resultado[i, 1] = media

        variancia = np.var(amostra)
        matriz_resultado[i, 2] = variancia

        maximo = np.max(amostra)
        matriz_resultado[i, 3] = maximo

        minimo = np.min(amostra)
        matriz_resultado[i, 4] = minimo

        amplitude = maximo-minimo
        matriz_resultado[i, 5] = amplitude

        print('Média: ' + str(media))
        print('Variância: ' + str(variancia))
        print('Máximo: ' + str(maximo))
        print('Minimo: ' + str(minimo))
        print('Amplitude: ' + str(amplitude))
        print('-----------------------------------------------------------------------------------------------------------------')

    return matriz_resultado
#print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
#vt = np.array([10, 20, 30, 40, 50, 25])
#resultado_amostragem = amostrar(vt,tamanho_amostra=3,numero_amostragens=1000)
#print('Resultado:')
#print('  Amostra     Média     Var     Máx      Mín      Amp')
#np.set_printoptions(precision=2)
#np.set_printoptions(suppress=True)
#print(str(resultado_amostragem))
#print('-----------------------------------------------------------------------------------------------------------------')

