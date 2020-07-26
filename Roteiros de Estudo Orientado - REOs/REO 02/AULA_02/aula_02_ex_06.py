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
# PROCEDIMENTO: Histogramas de imagens coloridas em YCRCB
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

#nome_arquivo = 'img_feijao.jpg'
nome_arquivo = 'feijao.jpg'

img_bgr = cv2.imread(nome_arquivo,1)
img_YCRCB = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

########################################################################################################################
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_Y = cv2.calcHist([img_YCRCB],[0],None,[256],[0,256])
hist_CR = cv2.calcHist([img_YCRCB],[1],None,[256],[0,256])
hist_CB = cv2.calcHist([img_YCRCB],[2],None,[256],[0,256])

########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap="gray")
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_YCRCB,cmap="gray")
plt.title("YCRCB")

plt.subplot(3,3,4)
plt.imshow(img_YCRCB[:,:,0],cmap='gray')
plt.title("Y")

plt.subplot(3,3,7)
plt.plot(hist_Y,color = 'black')
plt.title("Histograma - Y")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,5)
plt.imshow(img_YCRCB[:,:,1],cmap='gray')
plt.title("CR")

plt.subplot(3,3,8)
plt.plot(hist_CR,color = 'black')
plt.title("Histograma - CR")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,6)
plt.imshow(img_YCRCB[:,:,2],cmap='gray')
plt.title("CB")

plt.subplot(3,3,9)
plt.plot(hist_CB,color = 'black')
plt.title("Histograma - CB")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################