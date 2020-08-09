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
# Adaptado de: https://towardsdatascience.com/introduction-to-image-segmentation-with-k-means-clustering-83fd0a9e2fc3
########################################################################################################################
# Importação
import cv2
import numpy as np
from matplotlib import pyplot as plt
########################################################################################################################
# Leitura da imagem
nome_arquivo = 'macas.jpg'
img = cv2.imread(nome_arquivo,1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

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
print('SQ das Distâncias de Cada Ponto ao Centro: ', dist)
print('-'*80)
print('Dimensão labels: ', labels.shape)
print('Valores únicos: ',np.unique(labels))
print('Tipo labels: ', type(labels))
# flatten the labels array
labels = labels.flatten()
print('-'*80)
print('Dimensão flatten labels: ', labels.shape)
print('Tipo labels (f): ', type(labels))
print('-'*80)

# Valores dos labels
val_unicos,contagens = np.unique(labels,return_counts=True)
val_unicos = np.reshape(val_unicos,(len(val_unicos),1))
contagens = np.reshape(contagens,(len(contagens),1))
hist = np.concatenate((val_unicos,contagens),axis=1)
print('Histograma')
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
########################################################################################################################
# Conversão dos pixels para a cor dos centroides
matriz_segmentada = centers[labels]
print('-'*80)
print('Dimensão Matriz Segmentada: ',matriz_segmentada.shape)
print('Matriz Segmentada')
print(matriz_segmentada[0:5,:])
print('-'*80)
########################################################################################################################
# Reformatar a matriz na imagem de formato original
img_segmentada = matriz_segmentada.reshape(img.shape)

# Grupo 1
original_01 = np.copy(img)
matriz_or_01 = original_01.reshape((-1, 3))
matriz_or_01[labels != 0] = [0, 0, 0]
img_final_01 = matriz_or_01.reshape(img.shape)

# Grupo 2
original_02 = np.copy(img)
matriz_or_02 = original_02.reshape((-1, 3))
matriz_or_02[labels != 1] = [0, 0, 0]
img_final_02 = matriz_or_02.reshape(img.shape)

# Grupo 3
original_03 = np.copy(img)
matriz_or_03 = original_03.reshape((-1, 3))
matriz_or_03[labels != 2] = [0, 0, 0]
img_final_03 = matriz_or_03.reshape(img.shape)
########################################################################################################################

# Apresentar Imagem
plt.figure('Imagens')
plt.subplot(2,3,1)
plt.imshow(img)
plt.title('ORIGINAL')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(img_segmentada)
plt.title('ROTULOS')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(img_final_01)
plt.title('Grupo 1')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,5)
plt.imshow(img_final_02)
plt.title('Grupo 2')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,6)
plt.imshow(img_final_03)
plt.title('Grupo 3')
plt.xticks([])
plt.yticks([])

plt.show()

