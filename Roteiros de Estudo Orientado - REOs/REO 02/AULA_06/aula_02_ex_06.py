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
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Transformações em imagens
M_01 = np.float32([[1,0, 0],[0,1,500]])
img_tl1 = cv2.warpAffine(img,M_01,(img.shape[1],img.shape[0]))

M_02 = np.float32([[1,0, 0],[0,1,-500]])
img_tl2 = cv2.warpAffine(img,M_02,(img.shape[1],img.shape[0]))

M_03 = np.float32([[1,0, 500],[0,1,0]])
img_tl3 = cv2.warpAffine(img,M_03,(img.shape[1],img.shape[0]))

M_04 = np.float32([[1,0, -500],[0,1,0]])
img_tl4 = cv2.warpAffine(img,M_04,(img.shape[1],img.shape[0]))

M_05 = np.float32([[1,0, -500],[0,1,500]])
img_tl5 = cv2.warpAffine(img,M_05,(img.shape[1],img.shape[0]))

print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES TRANSLAÇÃO 500 PARA BAIXO E 500 PARA ESQUERDA')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canal = np.shape(img_tl5)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Canais: ' + str(canal))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('TRANSLAÇÃO')
plt.subplot(2,3,1)
plt.imshow(img)
plt.title("ORIGINAL")

plt.subplot(2,3,2)
plt.imshow(img_tl1)
plt.title("BAIXO")

plt.subplot(2,3,3)
plt.imshow(img_tl2)
plt.title("CIMA")

plt.subplot(2,3,4)
plt.imshow(img_tl3)
plt.title("DIREITA")

plt.subplot(2,3,5)
plt.imshow(img_tl4)
plt.title("ESQUERDA")

plt.subplot(2,3,6)
plt.imshow(img_tl5)
plt.title("BAIXO E ESQUERDA")

plt.show()
########################################################################################################################