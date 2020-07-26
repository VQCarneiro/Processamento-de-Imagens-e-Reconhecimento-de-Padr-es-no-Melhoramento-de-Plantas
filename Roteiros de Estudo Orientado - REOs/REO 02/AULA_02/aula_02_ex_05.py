########################################################################################################################
# Lavras - MG
# 20/06/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Professor: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# PROCEDIMENTO: Histogramas de imagens coloridas em HSV
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'

img_bgr = cv2.imread(nome_arquivo,1)
img_HSV = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2HSV)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

########################################################################################################################
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_H = cv2.calcHist([img_HSV],[0],None,[256],[0,256])
hist_S = cv2.calcHist([img_HSV],[1],None,[256],[0,256])
hist_V = cv2.calcHist([img_HSV],[2],None,[256],[0,256])

########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_HSV,cmap="gray")
plt.title("HSV")

plt.subplot(3,3,4)
plt.imshow(img_HSV[:,:,0],cmap='gray')
plt.title("H")

plt.subplot(3,3,7)
plt.plot(hist_H,color = 'black')
plt.title("Histograma - H")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_HSV[:,:,1],cmap='gray')
plt.title("S")

plt.subplot(3,3,8)
plt.plot(hist_S,color = 'black')
plt.title("Histograma - S")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_HSV[:,:,2],cmap='gray')
plt.title("V")

plt.subplot(3,3,9)
plt.plot(hist_V,color = 'black')
plt.title("Histograma - V")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################