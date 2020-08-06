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
########################################################################################################################
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import imutils
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
# compute the exact Euclidean distance from every binary
# pixel to the nearest zero pixel, then find peaks in this
# distance map
D = ndimage.distance_transform_edt(mascara)
localMax = peak_local_max(D, indices=False, min_distance=300,
	labels=mascara)
# perform a connected component analysis on the local peaks,
# using 8-connectivity, then appy the Watershed algorithm
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=mascara)
print("[INFO] {} unique segments found".format(len(np.unique(labels)) - 1))
img_final = np.copy(img_rgb)
img_final[labels != 3] = [0,0,0]
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
plt.imshow(D,cmap='jet')
plt.xticks([])
plt.yticks([])
plt.title('Distância')

plt.subplot(2,3,5)
plt.imshow(labels,cmap='jet')
plt.xticks([])
plt.yticks([])
plt.title('Batatas')

plt.subplot(2,3,6)
plt.imshow(img_final)
plt.xticks([])
plt.yticks([])
plt.title('SELEÇÃO')

plt.show()