########################################################################################################################
# Lavras - MG
# 21/04/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Processamento de imagens e reconhecimento de padrões no melhoramento de plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Escala de Cinza e Operações Aritiméticas em Imagens
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
vet = np.array([0,25,50,75,100,150,175,200,255],np.uint8)
print(vet)
mat = np.ones((2,9))
print('')
print(mat)
mat = mat*vet
print('')
print(mat)
plt.imshow(mat,cmap = "jet")
plt.show()
# ########################################################################################################################
# # Teste de soma e subtração de valores cujo o espaço amostral é entre 0 e 255: [0,255]
valor_01 = cv2.add(np.uint8([200]),np.uint8([100]))
print('')
print('Valor é ' + str(valor_01) + '. Máximo é 255')
#
valor_02 = cv2.subtract(np.uint8([50]),np.uint8([100]))
print('Valor é ' + str(valor_02) + '. Mínimo é 0')
########################################################################################################################

