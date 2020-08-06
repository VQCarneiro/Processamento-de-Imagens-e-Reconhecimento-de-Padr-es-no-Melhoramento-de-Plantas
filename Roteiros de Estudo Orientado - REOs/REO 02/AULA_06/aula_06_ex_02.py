########################################################################################################################
# Lavras - MG
# 21/06/2020
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
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
import imutils
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_YCrCb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)

########################################################################################################################
# Partição dos canais
Y,Cr,Cb = cv2.split(img_YCrCb)
########################################################################################################################
# Histograma do canal informativo
hist_Cr = cv2.calcHist([Cb],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding

(L, img_limiar) = cv2.threshold(Cb,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(L, img_limiar_inv) = cv2.threshold(Cb,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

########################################################################################################################
# Obtendo imagem segmentada
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_inv)

########################################################################################################################
# Contagem
cnts = cv2.findContours(img_limiar_inv.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DOS OBJETOS')
print('----------------------------------------------------------------------------------------------------------------')
print('NÚMERO DE SEMENTES: ' + str(len(cnts)))
print('----------------------------------------------------------------------------------------------------------------')

# loop over the contours
img_seg_editada = img_segmentada.copy()
for (i, c) in enumerate(cnts):
	# draw the contour
	((x, y), _) = cv2.minEnclosingCircle(c)
	cv2.putText(img_seg_editada, "#{}".format(i + 1), (int(x) - 10, int(y)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	cv2.drawContours(img_seg_editada, [c], -1, (0, 255, 0), 2)

img_rgb_editada = img_rgb.copy()
# loop over the contours
for (i, c) in enumerate(cnts):
	# draw the contour
	((x, y), _) = cv2.minEnclosingCircle(c)
	cv2.putText(img_rgb_editada, "#{}".format(i + 1), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	cv2.drawContours(img_rgb_editada, [c], -1, (0, 255, 0), 2)


########################################################################################################################
# Recortar cada semente
#img_segmentada_backup = img_segmentada.copy()
#img_segmentada = cv2.cvtColor(img_segmentada,cv2.COLOR_RGB2HSV)

plt.figure('Sementes')
for (i, c) in enumerate(cnts):

	(x,y,w,h) = cv2.boundingRect(c)
	print('Semente #%d' % (i+1))
	print(cv2.contourArea(c))
	obj = img_limiar_inv[y:y+h,x:x+w]
	obj_rgb = img_segmentada[y:y+h,x:x+w]

	grafico = True
	if grafico == True:

		hist_r = cv2.calcHist([obj_rgb[:,:,0]],[0],obj,[256],[0,256])
		hist_g = cv2.calcHist([obj_rgb[:,:,1]], [0],obj, [256], [0, 256])
		hist_b = cv2.calcHist([obj_rgb[:,:,2]], [0],obj, [256], [0, 256])
		#obj = img_rgb[y:y + h, x:x + w]

		plt.subplot(3,3,2)
		plt.imshow(obj_rgb)
		plt.title('Semente: ' + str(i+1))

		plt.subplot(3, 3, 4)
		plt.imshow(obj_rgb[:,:,0],cmap='gray')
		plt.title('Semente: ' + str(i + 1))

		plt.subplot(3, 3, 5)
		plt.imshow(obj_rgb[:,:,1],cmap='gray')
		plt.title('Semente: ' + str(i + 1))

		plt.subplot(3, 3, 6)
		plt.imshow(obj_rgb[:,:,2],cmap='gray')
		plt.title('Semente: ' + str(i + 1))

		plt.subplot(3, 3, 7)
		plt.plot(hist_r, color='r')
		plt.title("Histograma - R")
		plt.xlim([0, 256])
		plt.xlabel("Valores Pixels")
		plt.ylabel("Número de Pixels")

		plt.subplot(3, 3, 8)
		plt.plot(hist_g, color='g')
		plt.title("Histograma - R")
		plt.xlim([0, 256])
		plt.xlabel("Valores Pixels")
		plt.ylabel("Número de Pixels")

		plt.subplot(3, 3, 9)
		plt.plot(hist_r, color='r')
		plt.title("Histograma - B")
		plt.xlim([0, 256])
		plt.xlabel("Valores Pixels")
		plt.ylabel("Número de Pixels")


		plt.pause(1)
		#f.savefig(str(i+1)+'.png')
		plt.show(block = False)
		plt.clf()

	else:
		pass


########################################################################################################################
