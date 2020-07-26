########################################################################################################################
# Lavras - MG
# 20/06/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Thresholding - Limiar Manual
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'

img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
img_cinza = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

########################################################################################################################
# Histograma escala de cinza
hist_cinza = cv2.calcHist([img_cinza],[0], None, [256],[0,256])

########################################################################################################################
# Limiarização - Thresholding
limiar_cinza = 140
(L, img_limiar) = cv2.threshold(img_cinza,limiar_cinza,255,cv2.THRESH_BINARY)

(L, img_limiar_inv) = cv2.threshold(img_cinza,limiar_cinza,255,cv2.THRESH_BINARY_INV)

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DO AULA_03')
print('----------------------------------------------------------------------------------------------------------------')
print('Limiar: ' + str(L))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar figuras

plt.figure('Thresholding')
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title('RGB')

plt.subplot(2,3,2)
plt.imshow(img_cinza,cmap='gray')
plt.title('Escala de Cinza')

plt.subplot(2,3,3)
plt.plot(hist_cinza,color = 'black')
plt.axvline(x=limiar_cinza,color = 'r')
plt.title("Histograma - Cinza")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,3,4)
plt.imshow(img_limiar,cmap='gray')
plt.title('Binário - L: ' + str(limiar_cinza))

plt.subplot(2,3,5)
plt.imshow(img_limiar_inv,cmap='gray')
plt.title('Binário Invertido: L: ' + str(limiar_cinza))

plt.show()
########################################################################################################################