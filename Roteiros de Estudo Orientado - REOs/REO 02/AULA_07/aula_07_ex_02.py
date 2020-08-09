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
# PROCEDIMENTO: Filtros de detecção de bordas
########################################################################################################################
# Importar pacotes
import cv2
import numpy as np
from matplotlib import pyplot as plt
########################################################################################################################
# Leitura da imagem

#nome_arquivo = 'mascara.png'
#nome_arquivo = 'segmentada.png'
nome_arquivo = 'trabalho.jpeg'
img = cv2.imread(nome_arquivo,0)
########################################################################################################################
# Filtros
img_l = cv2.Laplacian(img,cv2.CV_64F)
abs_l64f = np.absolute(img_l)
img_l = np.uint8(abs_l64f)
img_sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sx64f = np.absolute(img_sx)
img_sx = np.uint8(abs_sx64f)
img_sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
abs_sy64f = np.absolute(img_sy)
img_sy = np.uint8(abs_sy64f)

# Detecção de bordas Canny
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