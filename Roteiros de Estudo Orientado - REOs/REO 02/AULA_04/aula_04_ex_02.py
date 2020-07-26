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
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_r = cv2.calcHist([img_rgb],[0],None,[256],[0,256])
hist_g = cv2.calcHist([img_rgb],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_rgb],[2],None,[256],[0,256])

########################################################################################################################
# Equalização do histograma

# R
eq_hist_r = cv2.equalizeHist(img_rgb[:,:,0])
hist_r_eq = cv2.calcHist([eq_hist_r],[0],None,[256],[0,256])

# G
eq_hist_g = cv2.equalizeHist(img_rgb[:,:,1])
hist_g_eq = cv2.calcHist([eq_hist_g],[0],None,[256],[0,256])

# B
eq_hist_b = cv2.equalizeHist(img_rgb[:,:,2])
hist_b_eq = cv2.calcHist([eq_hist_b],[0],None,[256],[0,256])

########################################################################################################################
# Modificando imagem

img_mod = np.copy(img_rgb)
img_mod[:,:,2] = eq_hist_b

########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_mod,cmap="gray")
plt.title("Modificações")

plt.subplot(3,3,4)
plt.imshow(eq_hist_r,cmap='gray')
plt.title("R")

plt.subplot(3,3,7)
plt.plot(hist_r_eq,color = 'r')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(eq_hist_g,cmap='gray')
plt.title("G")

plt.subplot(3,3,8)
plt.plot(hist_g_eq,color = 'g')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(eq_hist_b,cmap='gray')
plt.title("B")

plt.subplot(3,3,9)
plt.plot(hist_b_eq,color = 'blue')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################