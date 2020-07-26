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
# PROCEDIMENTO: Histogramas 2D de imagens coloridas
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
# Partição dos canais de uma imagem

r,g,b = cv2.split(img_rgb)

########################################################################################################################
# Histograma da imagem

# Histograma 1D
hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DOS AULA_02 1D')
print('----------------------------------------------------------------------------------------------------------------')
lin_r, col_r = np.shape(hist_r)
print('Dimensão: ' + str(lin_r) +' x '+ str(col_r))
print('----------------------------------------------------------------------------------------------------------------')

# Histograma 2D
hist_r_g = cv2.calcHist([r,g],[0,1],None,[32,32],[0,256,0,256])
hist_r_b = cv2.calcHist([r,b],[0,1],None,[32,32],[0,256,0,256])
hist_g_b = cv2.calcHist([g,b],[0,1],None,[32,32],[0,256,0,256])

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DOS AULA_02 2D')
print('----------------------------------------------------------------------------------------------------------------')
lin_r_g, col_r_g = np.shape(hist_r_g)
print('Dimensão: ' + str(lin_r_g) +' x '+ str(col_r_g))
print('----------------------------------------------------------------------------------------------------------------')

# Histograma 3D
hist_3D = cv2.calcHist([img_rgb],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DOS AULA_02 3D')
print('----------------------------------------------------------------------------------------------------------------')
lin_rgb, col_rgb, esp_rgb = np.shape(hist_3D)
print('Dimensão: ' + str(lin_rgb) +' x '+ str(col_rgb) + ' x ' + str(esp_rgb))
print('Número de valores: ' + str(hist_3D.flatten().shape[0]))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Apresentar figuras

# IMAGENS
plt.figure('IMAGEM')
plt.subplot(2,3,2)
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(2,3,4)
plt.imshow(img_rgb[:,:,0],cmap='gray')
plt.title("R")

plt.subplot(2,3,5)
plt.imshow(img_rgb[:,:,1],cmap='gray')
plt.title("G")

plt.subplot(2,3,6)
plt.imshow(img_rgb[:,:,2],cmap='gray')
plt.title("B")

# Histogramas
plt.figure('AULA_02')
plt.subplot(2,3,1)
plt.plot(hist_r,color = 'r')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,2)
plt.plot(hist_g,color = 'g')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,3)
plt.plot(hist_b,color = 'blue')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,4)
plt.imshow(hist_r_g,interpolation='nearest')
plt.title("R-G")
plt.colorbar()
plt.xlabel("R")
plt.ylabel("G")

plt.subplot(2,3,5)
plt.imshow(hist_r_b,interpolation='nearest')
plt.title("R-G")
plt.colorbar()
plt.xlabel("R")
plt.ylabel("B")

plt.subplot(2,3,6)
plt.imshow(hist_g_b,interpolation='nearest')
plt.title("R-G")
plt.colorbar()
plt.xlabel("G")
plt.ylabel("B")

plt.show()
########################################################################################################################