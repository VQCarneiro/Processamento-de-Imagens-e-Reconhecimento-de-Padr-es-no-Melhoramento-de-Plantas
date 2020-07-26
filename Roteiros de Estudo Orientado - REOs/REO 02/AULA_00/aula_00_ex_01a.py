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
# PROCEDIMENTO: Leitura e apresentação de uma imagem binária
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem
nome_arquivo = "img_quadrado.png" # Nome do arquivo a ser utilizado na análise
img_bin = cv2.imread(nome_arquivo,0) # Carrega imagem (0 - Binária e Escala de Cinza; 1 - Colorida (BGR))
########################################################################################################################
# Dados da Imagem
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM BINÁRIA')
print('----------------------------------------------------------------------------------------------------------------')
print(img_bin)
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_bin)
print('Tipo: ',img_bin.dtype)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
valor_pixel_00 = img_bin[0,0]
print("Valor do pixel da imagem original na posição (0,0): " + str(valor_pixel_00))
valor_pixel_12 = img_bin[1,2]
print("Valor do pixel da imagem original na posição (1,2): " + str(valor_pixel_12))
valor_pixel_55 = img_bin[5,5]
print("Valor do pixel da imagem modificada na posição (5,5): " + str(valor_pixel_55))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Apresentar imagens no matplotlib
plt.figure('Imagem Binária')
plt.imshow(img_bin,cmap="gray") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("Imagem Binária")
plt.show()
########################################################################################################################
