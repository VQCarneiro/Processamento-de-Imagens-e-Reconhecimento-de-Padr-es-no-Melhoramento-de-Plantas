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
# PROCEDIMENTO: Identificação e Mensuração de Objetos
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np
from matplotlib import pyplot as plt # Importa o pacote matplotlib
from skimage.measure import label, regionprops
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_YCrCb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)

########################################################################################################################
# Partição dos canais
Y,Cr,Cb = cv2.split(img_YCrCb)
Cb = cv2.medianBlur(Cb,9)
########################################################################################################################
# Histograma do canal informativo
hist_Cb = cv2.calcHist([Cb],[0], None, [256],[0,256])
########################################################################################################################
# Limiarização - Thresholding
(L, img_limiar_inv) = cv2.threshold(Cb,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
########################################################################################################################
# Obtendo imagem segmentada
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_inv)

########################################################################################################################
# Objetos
mascara = img_limiar_inv.copy()
cnts,h = cv2.findContours(mascara, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

########################################################################################################################
# Dados Sementes
print('-'*50)
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_properties/py_contour_properties.html

for (i, c) in enumerate(cnts):

	(x, y, w, h) = cv2.boundingRect(c)
	obj = img_limiar_inv[y:y+h,x:x+w]
	obj_rgb = img_segmentada[y:y+h,x:x+w]
	obj_bgr = cv2.cvtColor(obj_rgb,cv2.COLOR_RGB2BGR)
	cv2.imwrite('s'+str(i+1)+'.png',obj_bgr)
	cv2.imwrite('sb'+str(i+1)+'.png',obj)

	regiao = regionprops(obj) #https: // scikit - image.org / docs / dev / api / skimage.measure.html  # skimage.measure.regionprops
	print('Semente: ', str(i+1))
	print('Dimensão da Imagem: ', np.shape(obj))
	print('Medidas Físicas')
	print('Centroide: ', regiao[0].centroid)
	print('Comprimento do eixo menor: ', regiao[0].minor_axis_length)
	print('Comprimento do eixo maior: ', regiao[0].major_axis_length)
	print('Razão: ', regiao[0].major_axis_length / regiao[0].minor_axis_length)
	area = cv2.contourArea(c)
	print('Área: ', area)
	print('Perímetro: ', cv2.arcLength(c,True))

	print('Medidas de Cor')
	min_val_r, max_val_r, min_loc_r, max_loc_r = cv2.minMaxLoc(obj_rgb[:,:,0], mask=obj)
	print('Valor Mínimo no R: ', min_val_r, ' - Posição: ', min_loc_r)
	print('Valor Máximo no R: ', max_val_r, ' - Posição: ', max_loc_r)
	med_val_r = cv2.mean(obj_rgb[:,:,0], mask=obj)
	print('Média no Vermelho: ', med_val_r)

	min_val_g, max_val_g, min_loc_g, max_loc_g = cv2.minMaxLoc(obj_rgb[:, :, 1], mask=obj)
	print('Valor Mínimo no G: ', min_val_g, ' - Posição: ', min_loc_g)
	print('Valor Máximo no G: ', max_val_g, ' - Posição: ', max_loc_g)
	med_val_g = cv2.mean(obj_rgb[:,:,1], mask=obj)
	print('Média no Verde: ', med_val_g)

	min_val_b, max_val_b, min_loc_b, max_loc_b = cv2.minMaxLoc(obj_rgb[:, :, 2], mask=obj)
	print('Valor Mínimo no B: ', min_val_b, ' - Posição: ', min_loc_b)
	print('Valor Máximo no B: ', max_val_b, ' - Posição: ', max_loc_b)
	med_val_b = cv2.mean(obj_rgb[:,:,2], mask=obj)
	print('Média no Azul: ', med_val_b)
	print('-'*50)



########################################################################################################################
print('Total de sementes: ', len(cnts))
print('-'*50)

seg = img_segmentada.copy()
cv2.drawContours(seg,cnts,-1,(0,255,0),2)

plt.figure('Sementes')
plt.subplot(1,2,1)
plt.imshow(seg)
plt.xticks([])
plt.yticks([])
plt.title('Sementes')

plt.subplot(1,2,2)
plt.imshow(obj_rgb)
plt.xticks([])
plt.yticks([])
plt.title('Semente')
plt.show()
########################################################################################################################



