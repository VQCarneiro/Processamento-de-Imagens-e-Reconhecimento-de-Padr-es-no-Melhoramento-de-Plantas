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
# PROCEDIMENTO: Leitura e apresentação de uma imagem em escala de cinza
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = "img_cinza.png" # Nome do arquivo a ser utilizado na análise
img_cinza = cv2.imread(nome_arquivo,0) # Carrega imagem (0 - Binária e Escala de Cinza; 1 - Colorida (BGR))
########################################################################################################################
# Dados da Imagem
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM BINÁRIA')
print('----------------------------------------------------------------------------------------------------------------')
print(img_cinza)
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_cinza)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens no matplotlib
plt.figure('Imagens')
plt.subplot(1,2,1)
plt.imshow(img_cinza,cmap="gray") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
#plt.xticks([]) # Eliminar o eixo X
#plt.yticks([]) # Eliminar o eixo Y
plt.title("Escala de Cinza")
plt.colorbar(orientation = 'horizontal')

plt.subplot(1,2,2)
plt.imshow(img_cinza,cmap="jet") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
#plt.xticks([]) # Eliminar o eixo X
#plt.yticks([]) # Eliminar o eixo Y
plt.title("JET")
plt.colorbar(orientation = 'horizontal')

plt.show()
########################################################################################################################