########################################################################################################################
# Lavras - MG
# 08/04/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Processamento de imagens e reconhecimento de padrões no melhoramento de plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Translação em imagens coloridas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img = cv2.imread(nome_arquivo)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print('----------------------------------------------------------------------------------------------------------------')
print('IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canal = np.shape(img)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Canais: ' + str(canal))
centro = (round(col/2),round(lin/2))
print('Centro: ' + str(centro))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Transformações em imagens

M_01 = cv2.getRotationMatrix2D(centro,20,1.0)
img_rt1 = cv2.warpAffine(img,M_01,(col,lin))

M_02 = cv2.getRotationMatrix2D(centro,45,1.0)
img_rt2 = cv2.warpAffine(img,M_02,(col,lin))

M_03 = cv2.getRotationMatrix2D(centro,60,1.0)
img_rt3 = cv2.warpAffine(img,M_03,(col,lin))

M_04 = cv2.getRotationMatrix2D(centro,90,1.0)
img_rt4 = cv2.warpAffine(img,M_01,(col,lin))

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES ROTAÇÃO 90 GRAUS')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canal = np.shape(img_rt4)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Canais: ' + str(canal))
print('----------------------------------------------------------------------------------------------------------------')

M_05 = cv2.getRotationMatrix2D(centro,180,1.0)
img_rt5 = cv2.warpAffine(img,M_05,(col,lin))

########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('ROTAÇÃO')
plt.subplot(2,3,1)
plt.imshow(img)
plt.title("ORIGINAL")

plt.subplot(2,3,2)
plt.imshow(img_rt1)
plt.title("20")

plt.subplot(2,3,3)
plt.imshow(img_rt2)
plt.title("45")

plt.subplot(2,3,4)
plt.imshow(img_rt3)
plt.title("60")

plt.subplot(2,3,5)
plt.imshow(img_rt4)
plt.title("90")

plt.subplot(2,3,6)
plt.imshow(img_rt5)
plt.title("180")

plt.show()
########################################################################################################################