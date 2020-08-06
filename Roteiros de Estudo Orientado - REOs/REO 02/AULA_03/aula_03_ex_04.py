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
# PROCEDIMENTO: Segmentação
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_Lab = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2Lab)

########################################################################################################################
# Partição dos canais
L,a,b = cv2.split(img_Lab)
########################################################################################################################
# Histograma escala de cinza
hist_b = cv2.calcHist([b],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding
(L, img_limiar) = cv2.threshold(b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

########################################################################################################################
#'''
# Obtendo imagem segmentada
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar)

# Salvar imagens
img_segmentada_bgr = cv2.cvtColor(img_segmentada,cv2.COLOR_RGB2BGR)
cv2.imwrite('feijao_segmentada.png',img_segmentada_bgr)

hist_sementes_r = cv2.calcHist([img_segmentada],[0],img_limiar,[256],[0,256])
hist_sementes_g = cv2.calcHist([img_segmentada],[1],img_limiar,[256],[0,256])
hist_sementes_b = cv2.calcHist([img_segmentada],[2],img_limiar,[256],[0,256])

#'''
########################################################################################################################
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title('RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(b,cmap='gray')
plt.title('Lab - b')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.plot(hist_b,color = 'black')
plt.axvline(x=L,color = 'r')
plt.title("Histograma - b")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,4)
plt.imshow(img_limiar,cmap='gray')
plt.title('Limiar: ' + str(L))
plt.xticks([])
plt.yticks([])
plt.show()

#'''
plt.figure('Segmentação')
plt.subplot(3,3,1)
plt.imshow(img_rgb)
plt.title('RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(3,3,2)
plt.imshow(img_segmentada)
plt.title('Segmentada - RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(3,3,3)
plt.imshow(img_limiar,cmap = 'gray')
plt.title('Binarizada')
plt.xticks([])
plt.yticks([])

plt.subplot(3,3,4)
plt.imshow(img_segmentada[:,:,0],cmap = 'gray')
plt.title('Segmentada - R')
plt.xticks([])
plt.yticks([])

plt.subplot(3,3,5)
plt.imshow(img_segmentada[:,:,1],cmap = 'gray')
plt.title('Segmentada - G')
plt.xticks([])
plt.yticks([])

plt.subplot(3,3,6)
plt.imshow(img_segmentada[:,:,2],cmap = 'gray')
plt.title('Segmentada - B')
plt.xticks([])
plt.yticks([])

plt.subplot(3,3,7)
plt.plot(hist_sementes_r,color = 'r')
plt.title("Histograma - R")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,8)
plt.plot(hist_sementes_g,color = 'black')
plt.title("Histograma - G")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(3,3,9)
plt.plot(hist_sementes_b,color = 'b')
plt.title("Histograma - B")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")
plt.show()
#'''


########################################################################################################################