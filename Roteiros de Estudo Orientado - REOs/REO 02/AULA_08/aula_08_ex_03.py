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
import numpy as np
import cv2
from matplotlib import pyplot as plt
########################################################################################################################
img_bgr = cv2.imread('vermelho.jpeg',1)
#img_bgr = cv2.imread('feijao.jpg',1)
#img_bgr = cv2.imread('batata.jpg')
img_lab = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
L,a,b = cv2.split(img_lab)
#b = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)
limiar, mascara = cv2.threshold(a,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


########################################################################################################################
# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel, iterations = 20)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=5)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img_rgb,markers)
img_final = np.copy(img_rgb)

#img_final[markers == -1] = [0,255,0]

img_final[markers != 5] = [0,0,0]

print(np.unique(markers))

plt.figure('Watershed')
plt.subplot(3,3,1)
plt.imshow(img_rgb,cmap='gray')

plt.subplot(3,3,2)
plt.imshow(mascara,cmap='gray')

plt.subplot(3,3,3)
plt.imshow(opening,cmap='gray')

plt.subplot(3,3,4)
plt.imshow(sure_bg,cmap='gray')

plt.subplot(3,3,5)
plt.imshow(dist_transform,cmap='gray')

plt.subplot(3,3,6)
plt.imshow(sure_fg,cmap='gray')

plt.subplot(3,3,7)
plt.imshow(markers,cmap='jet')

plt.subplot(3,3,8)
plt.imshow(img_final)

plt.show()