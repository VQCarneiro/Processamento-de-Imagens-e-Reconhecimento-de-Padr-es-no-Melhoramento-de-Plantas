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
# PROCEDIMENTO: Adaptative Thresholding - Limiar adaptativo
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
img_cinza = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

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
# Histograma escala de cinza
hist_cinza = cv2.calcHist([img_cinza],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding

(L,img_otsu) = cv2.threshold(img_cinza,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(L,img_otsu_inv) = cv2.threshold(img_cinza,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DO AULA_03')
print('----------------------------------------------------------------------------------------------------------------')
print('Limiar: ' + str(L))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title('RGB')

plt.subplot(2,2,2)
plt.plot(hist_cinza,color = 'black')
plt.axvline(x=L,color = 'r')
plt.title("Histograma - Cinza")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,3)
plt.imshow(img_otsu,cmap='gray')
plt.title('Binário - L: ' + str(L))

plt.subplot(2,2,4)
plt.imshow(img_otsu_inv,cmap='gray')
plt.title('Binário Invertido: L: ' + str(L))

plt.show()
########################################################################################################################