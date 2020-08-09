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
# PROCEDIMENTO: Segmentação - Kmeans
########################################################################################################################
# Importação
import cv2
import numpy as np
from matplotlib import pyplot as plt
########################################################################################################################
# Leitura da imagem
nome_arquivo = 'img_seg.png'
img = cv2.imread(nome_arquivo,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

########################################################################################################################
print('-'*80)
print('INFORMAÇÕES')
print('-'*80)
print('Dimensão: ',np.shape(img))
print(np.shape(img)[0], ' x ',np.shape(img)[1], ' = ', np.shape(img)[0] * np.shape(img)[1])
print('-'*80)
########################################################################################################################
# Formatação da imagem para uma matriz de dados
pixel_values = img.reshape((-1, 3))
# Conversão para Decimal
pixel_values = np.float32(pixel_values)
print('-'*80)
print('Dimensão Matriz: ',pixel_values.shape)
print('-'*80)
########################################################################################################################
# K-means
# Critério de Parada
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
# Número de Grupos (k)
k = 3
dist, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
print('-'*80)
print('SQ das Distâncias de Cada Ponto ao Cento: ', dist)
print('-'*80)
print('Dimensão labels: ', labels.shape)
print('Valores únicos: ',np.unique(labels))
# flatten the labels array
labels = labels.flatten()
print('-'*80)
print('Dimensão flatten labels: ', labels.shape)
print('-'*80)

# Valores dos labels
val_unicos,contagens = np.unique(labels,return_counts=True)
val_unicos = np.reshape(val_unicos,(len(val_unicos),1))
contagens = np.reshape(contagens,(len(contagens),1))
hist = np.concatenate((val_unicos,contagens),axis=1)
print('Histogramas')
print(hist)
print('-'*80)
print('Centroides Decimais')
print(centers)
print('-'*80)
# Conversão dos centroides para valores de interos de 8 digitos
centers = np.uint8(centers)
print('-'*80)
print('Centroides uint8')
print(centers)
print('-'*80)

# Conversão dos pixels para a cor dos centroides
matriz_segmentada = centers[labels.flatten()]
print('-'*80)
print('Dimensão Matriz Segmentada: ',matriz_segmentada.shape)
print('-'*80)
print('Valores Únicos Coluna 1: ', np.unique(matriz_segmentada[:,0]))
print('-'*80)

# Reformatar a matriz na imagem de formato original
img_segmentada = matriz_segmentada.reshape(img.shape)


original_01 = np.copy(img)
matriz_or_01 = original_01.reshape((-1, 3))
cluster = 0
matriz_or_01[labels == cluster] = [0, 0, 0]
img_final_01 = matriz_or_01.reshape(img.shape)

original_02 = np.copy(img)
matriz_or_02 = original_02.reshape((-1, 3))
cluster = 1
matriz_or_02[labels == cluster] = [0, 0, 0]
img_final_02 = matriz_or_02.reshape(img.shape)

original_03 = np.copy(img)
matriz_or_03 = original_03.reshape((-1, 3))
cluster = 2
matriz_or_03[labels == cluster] = [0, 0, 0]
img_final_03 = matriz_or_03.reshape(img.shape)

# Apresentar Imagem
plt.figure('Imagens')
plt.subplot(2,3,2)
plt.imshow(img_segmentada)
plt.subplot(2,3,4)
plt.imshow(img_final_01)
plt.subplot(2,3,5)
plt.imshow(img_final_02)
plt.subplot(2,3,6)
plt.imshow(img_final_03)
plt.show()


'''
# disable only the cluster number 2 (turn the pixel into black)
masked_image = np.copy(image)
# convert to the shape of a vector of pixel values
masked_image = masked_image.reshape((-1, 3))
# color (i.e cluster) to disable
cluster = 2
masked_image[labels == cluster] = [0, 0, 0]
# convert back to original shape
masked_image = masked_image.reshape(image.shape)
# show the image

plt.imshow(masked_image)
plt.show()
'''