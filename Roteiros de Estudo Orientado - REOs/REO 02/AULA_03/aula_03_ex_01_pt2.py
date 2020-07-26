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
# PROCEDIMENTO: Thresholding - Limiar Manual
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'

img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(img_rgb)
########################################################################################################################
# Histograma escala de cinza

hist_r = cv2.calcHist([img_rgb],[0], None, [256],[0,256])
hist_g = cv2.calcHist([img_rgb],[1], None, [256],[0,256])
hist_b = cv2.calcHist([img_rgb],[2], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding
limiar_r = 80
(L_r, img_limiar_r) = cv2.threshold(r,limiar_r,255,cv2.THRESH_BINARY)

limiar_g = 200
(L_g, img_limiar_g) = cv2.threshold(g,limiar_g,255,cv2.THRESH_BINARY)

limiar_b = 120
(L_b, img_limiar_b) = cv2.threshold(b,limiar_b,255,cv2.THRESH_BINARY)

########################################################################################################################
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(3,3,1)
plt.imshow(r,cmap='gray')
plt.title('R')

plt.subplot(3,3,2)
plt.imshow(g,cmap='gray')
plt.title('G')

plt.subplot(3,3,3)
plt.imshow(b,cmap='gray')
plt.title('B')

plt.subplot(3,3,4)
plt.plot(hist_r,color = 'r')
plt.axvline(x=limiar_r,color = 'r')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.plot(hist_g,color = 'g')
plt.axvline(x=limiar_g,color = 'g')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.plot(hist_b,color = 'b')
plt.axvline(x=limiar_b,color = 'b')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,7)
plt.imshow(img_limiar_r,cmap='gray')
plt.title('Binário - L: ' + str(limiar_r))

plt.subplot(3,3,8)
plt.imshow(img_limiar_g,cmap='gray')
plt.title('Binário - L: ' + str(limiar_g))

plt.subplot(3,3,9)
plt.imshow(img_limiar_b,cmap='gray')
plt.title('Binário - L: ' + str(limiar_b))


plt.show()
########################################################################################################################