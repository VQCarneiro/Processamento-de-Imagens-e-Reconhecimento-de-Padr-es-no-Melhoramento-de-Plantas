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
# PROCEDIMENTO: Identificação de Objetos
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np
from matplotlib import pyplot as plt # Importa o pacote matplotlib
import imutils
from skimage.measure import label, regionprops
import skimage
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'mascara.png'
nome_arquivo = 'segmentada.png'
img = cv2.imread(nome_arquivo,0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
########################################################################################################################
# Transformações Morfológicas

kernel = np.ones((5,5),np.uint8)
# Erosão
img_e = cv2.erode(img,kernel,iterations = 10)
# Dilatação
img_d = cv2.dilate(img,kernel,iterations = 10)

# Abertura - Erosão seguida por dilatação
img_ruido = skimage.util.random_noise(img, mode="s&p")
img_a = cv2.morphologyEx(img_ruido, cv2.MORPH_OPEN, kernel)

# Fechamento - Dilatação seguida por erosão
img_f = cv2.morphologyEx(img_a, cv2.MORPH_CLOSE, kernel)

#Gradiente morfológico - Diferença entre dilatação e eroção
img_g = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
########################################################################################################################
# Resultados
plt.figure('Transformações Morfológicas')

plt.subplot(3,3,1)
plt.imshow(img,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('ORIGINAL')

plt.subplot(3,3,2)
plt.imshow(img_e,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Erosão')

plt.subplot(3,3,3)
plt.imshow(img_d,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Dilatação')

plt.subplot(3,3,4)
plt.imshow(img_ruido,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Ruido')

plt.subplot(3,3,5)
plt.imshow(img_a,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Abertura')

plt.subplot(3,3,6)
plt.imshow(img_f,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Fechamento')

plt.subplot(3,3,7)
plt.imshow(img_g,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Gradiente')

plt.show()