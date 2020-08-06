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

#nome_arquivo = 'mascara.png'
nome_arquivo = 'segmentada.png'
#nome_arquivo = 'trabalho.jpeg'
img = cv2.imread(nome_arquivo,0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
########################################################################################################################
# Filtros
img_l = cv2.Laplacian(img,cv2.CV_64F)
img_sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# DEtecção de bordas Canny
edges = cv2.Canny(img,100,200)
########################################################################################################################
# Resultados
plt.figure('Transformações Morfológicas')

plt.subplot(2,3,1)
plt.imshow(img,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('ORIGINAL')

plt.subplot(2,3,2)
plt.imshow(img_l,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Laplaciano')

plt.subplot(2,3,3)
plt.imshow(img_sx,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Sobel X')

plt.subplot(2,3,4)
plt.imshow(img_sy,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Sobel Y')

plt.subplot(2,3,5)
plt.imshow(edges,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Canny')

plt.show()