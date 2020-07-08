########################################################################################################################
# DATA: 03/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# AULA 06
# TEMA: Módulos e Funções importantes
########################################################################################################################
'''
#Exemplo 01: Sequências no Python
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exemplo 01 - Sequências')
print('-----------------------------------------------------------------------------------------------------------------')

seq = range(0,10,1)
print('Sequência: ' + str(seq))
print('Tipo')
print(type(seq))
print('Dimensão: ' + str(len(seq)))

print('-----------------------------------------------------------------------------------------------------------------')

# Transformando o range em lista
lista_seq = list(seq)
print('Transformação em Lista')
print(lista_seq)

print('-----------------------------------------------------------------------------------------------------------------')

maximo = max(lista_seq)
print('Máximo: ' + str(maximo))
minimo = min(lista_seq)
print('Mínimo: ' + str(minimo))
somatorio = sum(lista_seq)
print('Somatório: ' + str(somatorio))

print('-----------------------------------------------------------------------------------------------------------------')

import math
raiz_quadrada = math.sqrt(lista_seq[-1])
print('Raiz Quadrada de 9: ' +str(raiz_quadrada))

print('-----------------------------------------------------------------------------------------------------------------')

import random
print('Lista: '+str(lista_seq))

lista_seq_aleatoria = random.sample(lista_seq,len(lista_seq)) #Aleatorização
print('Aleatorização: ' +str(lista_seq_aleatoria))

amostra_aleatoria = random.sample(lista_seq,4)
print('Amosta aleatória: ' + str(amostra_aleatoria))

amostra_aleatoria_ord = sorted(amostra_aleatoria,reverse=False)
print('Amostra Ordenada: ' + str(amostra_aleatoria_ord))
print('-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
########################################################################################################################




