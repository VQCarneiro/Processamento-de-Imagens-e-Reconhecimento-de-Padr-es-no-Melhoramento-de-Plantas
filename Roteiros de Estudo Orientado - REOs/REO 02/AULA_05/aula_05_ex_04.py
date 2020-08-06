########################################################################################################################
# Lavras - MG
# 02/08/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# PROCEDIMENTO: Filtros
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
# Filtro de Mediana
r_mediana = cv2.medianBlur(r,45)
g_mediana = cv2.medianBlur(g,45)
b_mediana = cv2.medianBlur(b,45)
########################################################################################################################
# Apresentar imagens no matplotlib
plt.figure('Filtro Média')
plt.subplot(2,3,1)
plt.imshow(r,cmap='gray')
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("R")

plt.subplot(2,3,2)
plt.imshow(g,cmap='gray')
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("G")

plt.subplot(2,3,3)
plt.imshow(b,cmap='gray')
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("B")

plt.subplot(2,3,4)
plt.imshow(r_mediana,cmap='gray')
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("R Mediana")

plt.subplot(2,3,5)
plt.imshow(g_mediana,cmap='gray')
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("G Mediana")

plt.subplot(2,3,6)
plt.imshow(b_mediana,cmap='gray')
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("B Mediana")
plt.show()
########################################################################################################################
#Histogramas

hist_r = cv2.calcHist([r],[0], None, [256],[0,256])
l,img_l = cv2.threshold(r,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
hist_r_mediana = cv2.calcHist([r_mediana],[0], None, [256],[0,256])
l_f,img_l_f = cv2.threshold(r_mediana,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

########################################################################################################################
#Figura
plt.figure('Histogramas')
plt.subplot(2,3,1)
plt.imshow(r,cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)
plt.plot(hist_r,color = 'r')
plt.axvline(x=l,color = 'k')
plt.title("L: "+str(l))
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,3)
plt.imshow(img_l,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Máscara')

plt.subplot(2,3,4)
plt.imshow(r_mediana,cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.plot(hist_r_mediana,color = 'r')
plt.axvline(x=l_f,color = 'k')
plt.title("L: " + str(l_f))
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,6)
plt.imshow(img_l_f,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Máscara')


plt.show()
########################################################################################################################



