########################################################################################################################
# Lavras - MG
# 13/07/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Processamento de imagens e reconhecimento de padrões no melhoramento de plantas
# Professor: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# PROCEDIMENTO: Manipulação de valores dos pixels em imagens coloridas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Manipulação de pixels em imagens
########################################################################################################################
# Leitura da imagem
nome_arquivo = 'img_quadrados_cores.png' # Nome do arquivo a ser utilizado na análise
img_bgr = cv2.imread(nome_arquivo, 1) # Carrega imagem colorida ou em escala de cinza
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
print('----------------------------------------------------------------------------------------------------------------')
print('MATRIZES DA IMAGEM ORIGINAL NO ESPAÇO DE COR RGB')
print('----------------------------------------------------------------------------------------------------------------')
print('MATRIZ R')
print('----------------------------------------------------------------------------------------------------------------')
print(img_rgb[:,:,0])
print('----------------------------------------------------------------------------------------------------------------')
print('MATRIZ G')
print('----------------------------------------------------------------------------------------------------------------')
print(img_rgb[:,:,1])
print('----------------------------------------------------------------------------------------------------------------')
print('MATRIZ B')
print('----------------------------------------------------------------------------------------------------------------')
print(img_rgb[:,:,2])
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canal = np.shape(img_rgb)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print("Número de canais: " + str(canal))
print('----------------------------------------------------------------------------------------------------------------')
print('VALORES PIXELS')
print('----------------------------------------------------------------------------------------------------------------')
valor_pixel_00 = img_rgb[0,0]
print("Valores  do pixel da imagem original na posição (0,0): " + str(valor_pixel_00))
valor_pixel_22 = img_rgb[2,2]
print("Valores  do pixel da imagem original na posição (2,2): " + str(valor_pixel_22))
valor_pixel_55 = img_rgb[5,5]
print("Valores  do pixel da imagem original na posição (5,5): " + str(valor_pixel_55))
valor_pixel_88 = img_rgb[8,8]
print("Valores  do pixel da imagem original na posição (8,8): " + str(valor_pixel_88))
valor_pixel_71 = img_rgb[7,1]
print("Valores  do pixel da imagem original na posição (7,1): " + str(valor_pixel_71))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Primeira Modificação na imagem
print('----------------------------------------------------------------------------------------------------------------')
print('MODIFICAÇÕES NA IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
img_mod_01=np.copy(img_rgb)
img_mod_01[2,2,0] = 255
valor_pixel_22_mod_01 = img_mod_01[2,2]
print("Valores do pixel da imagem modificada na posição (2,2): " + str(valor_pixel_22_mod_01))

img_mod_01[5,5,2] = 255
valor_pixel_55_mod_01 = img_mod_01[5,5]
print("Valor do pixel da imagem modificada na posição (5,5): " + str(valor_pixel_55_mod_01))

img_mod_01[8,8,1] = 255
valor_pixel_71_mod_01 = img_mod_01[8,8]
print("Valor do pixel da imagem modificada na posição (8,8): " + str(valor_pixel_71_mod_01))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentação das imagens
plt.figure("Imagens")
plt.subplot(1,2,1)
plt.imshow(img_rgb)
plt.xticks(np.arange(0,10,1))
plt.xticks(np.arange(0,10,1))
plt.title("ORIGINAL")

plt.subplot(1,2,2)
plt.imshow(img_mod_01)
plt.title("MODIFICAÇÃO")
plt.xticks(np.arange(0,10,1))
plt.xticks(np.arange(0,10,1))
plt.show()

########################################################################################################################