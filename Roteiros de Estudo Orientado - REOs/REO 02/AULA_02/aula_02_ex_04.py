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
# PROCEDIMENTO: Histogramas de imagens coloridas Lab
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'

img_bgr = cv2.imread(nome_arquivo,1)
img_Lab = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2Lab)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

########################################################################################################################
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_L = cv2.calcHist([img_Lab],[0],None,[256],[0,256])
hist_a = cv2.calcHist([img_Lab],[1],None,[256],[0,256])
hist_b = cv2.calcHist([img_Lab],[2],None,[256],[0,256])

########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_Lab,cmap="gray")
plt.title("Lab")

plt.subplot(3,3,4)
plt.imshow(img_Lab[:,:,0],cmap='gray')
plt.title("L")

plt.subplot(3,3,7)
plt.plot(hist_L,color = 'black')
plt.title("Histograma - L")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_Lab[:,:,1],cmap='gray')
plt.title("a")

plt.subplot(3,3,8)
plt.plot(hist_a,color = 'black')
plt.title("Histograma - a")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_Lab[:,:,2],cmap='gray')
plt.title("b")

plt.subplot(3,3,9)
plt.plot(hist_b,color = 'black')
plt.title("Histograma - b")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################