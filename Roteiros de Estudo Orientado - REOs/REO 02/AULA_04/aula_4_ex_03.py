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
# PROCEDIMENTO: Operações entre canais de imagens coloridas
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
########################################################################################################################
# Operações nos canais de uma imagem
img_opr_01 = img_rgb[:,:,2]-1.2*img_rgb[:,:,1]
# Conversão para inteiro de 8 bits
img_opr_01 = img_opr_01.astype(np.uint8)
# Histograma
hist = cv2.calcHist([img_opr_01],[0],None,[256],[0,256])
# Limiarização OTSU
(L,img_otsu) = cv2.threshold(img_opr_01,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Segmentação - máscara
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_otsu)

########################################################################################################################
# Apresentar imagens

# Figura das modificações

plt.figure('MODIFICAÇÕES')
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title("RGB")

plt.subplot(2,3,2)
plt.imshow(img_opr_01,cmap='gray')
plt.title("B - 1.2G")

plt.subplot(2,3,3)
plt.plot(hist,color = 'black')
plt.axvline(x=L,c = 'black')
plt.title("Histograma - L: " + str(L))
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,4)
plt.imshow(img_otsu,cmap='gray')
plt.title('Binária')

plt.subplot(2,3,5)
plt.imshow(img_segmentada,cmap='gray')
plt.title("Segmentada")
plt.xticks([])
plt.yticks([])

plt.show()
########################################################################################################################