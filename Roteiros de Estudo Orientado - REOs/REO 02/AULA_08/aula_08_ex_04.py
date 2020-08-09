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
# PROCEDIMENTO: Segmentação Watershed
# Adaptado de: https://www.pyimagesearch.com/2015/11/02/watershed-opencv/
# http://www.cmm.mines-paristech.fr/~beucher/wtshed.html
########################################################################################################################
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage
########################################################################################################################
#img_bgr = cv2.imread('vermelho.jpeg')
img_bgr = cv2.imread('batata.jpg')
img_ycrcb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
y,cr,cb = cv2.split(img_ycrcb)

limiar, mascara = cv2.threshold(cr,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

########################################################################################################################
img_dist = ndimage.distance_transform_edt(mascara) # https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.distance_transform_edt.html
# ndimage.distance_transform_edt: Calcula a distância euclidiana até o zero
# mais próximo (ou seja, pixel de fundo)para cada um dos pixels de primeiro plano.

max_local = peak_local_max(img_dist, indices=False, min_distance=300,
	labels=mascara)
# peak_local_max: retorna uma matriz booleana com os picos da imagem
# baseados nas distâncias
# min_distance: Número mínimo de pixels que separam os picos
# https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.peak_local_max
print('-'*50)
print('Número de Picos')
print(np.unique(max_local,return_counts=True))
print('-'*50)

marcadores,n_marcadores = ndimage.label(max_local, structure=np.ones((3, 3)))
# Realiza marcação dos picos
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html
# https://en.wikipedia.org/wiki/Connected-component_labeling
print('Análise de conectividade - Marcadores')
print(np.unique(marcadores,return_counts=True))
print('-'*50)

img_ws = watershed(-img_dist, marcadores, mask=mascara)
# https://scikit-image.org/docs/dev/api/skimage.segmentation.html#skimage.segmentation.watershed
# https://en.wikipedia.org/wiki/Watershed_(image_processing)
# https://scikit-image.org/docs/dev/auto_examples/segmentation/plot_watershed.html

print('Imagem Segmentada - Watershed')
print(np.unique(img_ws,return_counts=True))
print("Número de Batatas: ", len(np.unique(img_ws)) - 1)
print('-'*50)

img_final = np.copy(img_rgb)
img_final[img_ws != 3] = [0,0,0] # Acessando a batata 3
########################################################################################################################
plt.figure('Watershed')
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.xticks([])
plt.yticks([])
plt.title('ORIGINAL')

plt.subplot(2,3,2)
plt.imshow(cr,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Cr')

plt.subplot(2,3,3)
plt.imshow(mascara,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Mascara')

plt.subplot(2,3,4)
plt.imshow(img_dist,cmap='jet')
plt.xticks([])
plt.yticks([])
plt.title('Distância')

plt.subplot(2,3,5)
plt.imshow(img_ws,cmap='jet')
plt.xticks([])
plt.yticks([])
plt.title('Batatas')

plt.subplot(2,3,6)
plt.imshow(img_final)
plt.xticks([])
plt.yticks([])
plt.title('SELEÇÃO')

plt.show()