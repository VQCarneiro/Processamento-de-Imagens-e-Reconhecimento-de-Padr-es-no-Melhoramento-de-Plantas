########################################################################################################################
# Lavras - MG
# 13/07/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Professor: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# PROCEDIMENTO: Histogramas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'img_quadrado.png'
img = cv2.imread(nome_arquivo,0)
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DA IMAGEM')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Histograma da imagem
histograma = cv2.calcHist([img],[0],None,[256],[0,256])
print('----------------------------------------------------------------------------------------------------------------')
print('Histograma')
print(histograma)
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES DA IMAGEM')
print('----------------------------------------------------------------------------------------------------------------')
dim = len(histograma)
print('Dimensão do Histograma: ',dim)
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens

plt.figure('IMAGEM')
plt.subplot(1,2,1)
plt.imshow(img,cmap="gray")
plt.title("IMAGEM")

plt.subplot(1,2,2)
plt.plot(histograma,color = 'black')
plt.title("Histograma")
plt.xlabel("Valores Pixels")
plt.ylabel("Número de Pixels")

plt.show()
########################################################################################################################