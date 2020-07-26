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
# PROCEDIMENTO: Thresholding - Limiar Otsu
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_cinza = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

########################################################################################################################
# Histograma escala de cinza
hist_cinza = cv2.calcHist([img_cinza],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding - OTSU

(L,img_otsu) = cv2.threshold(img_cinza,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

########################################################################################################################
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.title('RGB')

plt.subplot(2,2,2)
plt.imshow(img_cinza,cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.plot(hist_cinza,color = 'black')
plt.axvline(x=L,color = 'r')
plt.title("Histograma - Cinza")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,4)
plt.imshow(img_otsu,cmap='gray')
plt.title('OTSU - L: ' + str(L))
plt.xticks([])
plt.yticks([])

plt.show()
########################################################################################################################