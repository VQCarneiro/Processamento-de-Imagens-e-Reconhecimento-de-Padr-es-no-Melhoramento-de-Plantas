########################################################################################################################
# Lavras - MG
# 20/06/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Thresholding - Limiar
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'img_feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_Lab = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2Lab)

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
# Partição dos canais
L,a,b = cv2.split(img_Lab)
########################################################################################################################
# Histograma escala de cinza
hist_b = cv2.calcHist([b],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding
(L, img_limiar) = cv2.threshold(b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(L, img_limiar_inv) = cv2.threshold(b,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DO AULA_03')
print('----------------------------------------------------------------------------------------------------------------')
print('Limiar: ' + str(L))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Obtendo imagem segmentada
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar)

########################################################################################################################
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title('RGB')

plt.subplot(2,2,2)
plt.plot(hist_b,color = 'black')
plt.axvline(x=L,color = 'r')
plt.title("Histograma - b")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,3)
plt.imshow(img_limiar,cmap='gray')
plt.title('Limiar: ' + str(L))

plt.subplot(2,2,4)
plt.imshow(img_limiar_inv,cmap='gray')
plt.title('Limiar: ' + str(L))

plt.figure('Segmentação')
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.title('RGB')

plt.subplot(1,2,2)
plt.imshow(img_segmentada)
plt.title('Segmentada')

plt.show()
########################################################################################################################