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
img_cinza = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DA IMAGEM')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais = np.shape(img_rgb)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Canais: ' + str(canais))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_cinza = cv2.calcHist([img_cinza],[0],None,[256],[0,256])

# Histograma de imagem em escala de cinza
hist_r = cv2.calcHist([img_rgb],[0],None,[256],[0,256])
hist_g = cv2.calcHist([img_rgb],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_rgb],[2],None,[256],[0,256])

########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(2,2,1)
plt.imshow(img_rgb,cmap="gray")
plt.xticks([])
plt.yticks([])
plt.title("RGB")

plt.subplot(2,2,2)
plt.imshow(img_cinza,cmap="gray")
plt.xticks([])
plt.yticks([])
plt.title("Escala de Cinza")

plt.subplot(2,2,3)
plt.plot(hist_r,color = 'r')
plt.plot(hist_g,color = 'g')
plt.plot(hist_b,color = 'b')
plt.title("Histograma RGB")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,4)
plt.plot(hist_cinza,color = 'black')
plt.title("Histograma Cinza")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################