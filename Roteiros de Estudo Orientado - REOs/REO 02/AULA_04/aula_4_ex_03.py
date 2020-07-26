########################################################################################################################
# Lavras - MG
# 19/06/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Histogramas de imagens coloridas e em escala de cinza
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DA IMAGEM')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais = np.shape(img_bgr)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Canais: ' + str(canais))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Operações nos canais de uma imagem
#img_opr_01 = np.uint8(1.5*img_rgb[:,:,2]) - np.uint8(2*img_rgb[:,:,0])
img_opr_01 = 1.5*img_rgb[:,:,2] - 2*img_rgb[:,:,0]
img_opr_02 = 1.5*img_rgb[:,:,2] - 1.5*img_rgb[:,:,0]
img_opr_03 = 1.8*img_rgb[:,:,2] - 1.5*img_rgb[:,:,0] - img_rgb[:,:,1]
print(img_opr_01)
#img_opr_01 = img_opr_01.astype(np.uint8)
#print(img_opr_01.astype(np.uint8))

########################################################################################################################
# Apresentar imagens

# Figura das modificações

plt.figure('MODIFICAÇÕES')
plt.subplot(2,2,1)
plt.imshow(img_rgb,cmap='gray')
plt.title("RGB")

plt.subplot(2,2,2)
plt.imshow(img_opr_01,cmap='gray')
plt.title("1.5B-2R")

plt.subplot(2,2,3)
plt.imshow(img_opr_02,cmap='gray')
plt.title("1.5B-1.5R")

plt.subplot(2,2,4)
plt.imshow(img_opr_03,cmap='gray')
plt.title("1.8B-1.5R-G")

plt.show()
########################################################################################################################