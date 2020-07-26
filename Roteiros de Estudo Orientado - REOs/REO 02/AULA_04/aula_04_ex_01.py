########################################################################################################################
# Lavras - MG
# 19/06/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Histogramas de imagens coloridas e em escala de cinza
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
img_cinza = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

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
# Histograma da imagem

# Histograma de imagem em escala de cinza
hist_cinza = cv2.calcHist([img_cinza],[0],None,[256],[0,256])

# Equalização do Histograma
eq_hist = cv2.equalizeHist(img_cinza)
hist_cinza_eq = cv2.calcHist([eq_hist],[0],None,[256],[0,256])
########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(2,2,1)
plt.imshow(img_cinza,cmap="gray")
plt.title("Imagem Original")

plt.subplot(2,2,2)
plt.plot(hist_cinza,color = 'black')
plt.title("Histograma Original")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.subplot(2,2,3)
plt.imshow(eq_hist,cmap="gray")
plt.title("Imagem Equalizada")

plt.subplot(2,2,4)
plt.plot(hist_cinza_eq,color = 'black')
plt.title("Histograma Equalizado - Cinza")
plt.xlim([0,256])
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################