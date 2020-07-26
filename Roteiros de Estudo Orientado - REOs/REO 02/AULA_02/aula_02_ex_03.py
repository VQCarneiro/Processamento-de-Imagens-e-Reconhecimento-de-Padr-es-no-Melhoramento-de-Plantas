########################################################################################################################
# Lavras - MG
# 13/07/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Professor: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# PROCEDIMENTO: Histogramas de imagens coloridas
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
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_r = cv2.calcHist([img_rgb],[0],None,[256],[0,256])
hist_g = cv2.calcHist([img_rgb],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_rgb],[2],None,[256],[0,256])

########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,2)
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,4)
plt.imshow(img_rgb[:,:,0],cmap='gray')
plt.title("R")

plt.subplot(3,3,7)
plt.plot(hist_r,color = 'r')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_rgb[:,:,1],cmap='gray')
plt.title("G")

plt.subplot(3,3,8)
plt.plot(hist_g,color = 'g')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_rgb[:,:,2],cmap='gray')
plt.title("B")

plt.subplot(3,3,9)
plt.plot(hist_b,color = 'blue')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################