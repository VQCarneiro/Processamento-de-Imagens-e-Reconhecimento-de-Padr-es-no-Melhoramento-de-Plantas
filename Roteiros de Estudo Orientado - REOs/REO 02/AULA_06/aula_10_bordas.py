########################################################################################################################
# Lavras - MG
# 21/06/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Detecção de bordas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_YCrCb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCR_CB)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DA IMAGEM')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais = np.shape(img_bgr)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Canais: ' + str(canais))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Partição dos canais
Y,Cr,Cb = cv2.split(img_YCrCb)

########################################################################################################################
bordas = cv2.Canny(Cr,5,11)

'''
########################################################################################################################
# Histograma do canal informativo
hist_Cr = cv2.calcHist([Cb],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding

(L, img_limiar) = cv2.threshold(Cb,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(L, img_limiar_inv) = cv2.threshold(Cb,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DO LIMIAR')
print('----------------------------------------------------------------------------------------------------------------')
print('Limiar: ' + str(L))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Obtendo imagem segmentada
img_segmentada = cv2.bitwise_and(img_rgb,img_rgb,mask=img_limiar_inv)
'''
########################################################################################################################
# Apresentar figuras

plt.figure('Bordas')
plt.subplot(1,3,1)
plt.imshow(img_rgb)
plt.title('RGB')

plt.subplot(1,3,2)
plt.imshow(Cr,cmap='gray')
plt.title('Cr')

plt.subplot(1,3,3)
plt.imshow(bordas,cmap='gray')
plt.title('Canny')



plt.show()
########################################################################################################################