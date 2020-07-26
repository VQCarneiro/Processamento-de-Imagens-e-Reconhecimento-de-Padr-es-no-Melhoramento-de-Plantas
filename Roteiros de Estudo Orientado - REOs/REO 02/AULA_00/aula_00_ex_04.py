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
# PROCEDIMENTO: Recorte de Imagens
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem
nome_arquivo = "img_cinza.png" # Nome do arquivo a ser utilizado na análise
img_intensidade = cv2.imread(nome_arquivo,0) # Carrega imagem (0 - Binária e Escala de Cinza; 1 - Colorida (BGR))
########################################################################################################################
# Dados da Imagem
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_intensidade)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Recortar uma imagem
img_recorte = img_intensidade[350:,0:800]
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES IMAGEM RECORTE')
print('----------------------------------------------------------------------------------------------------------------')
lin_r, col_r = np.shape(img_recorte)
print('Dimensão: ' + str(lin_r) +' x '+ str(col_r))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens no matplotlib
plt.figure('Imagens')
plt.subplot(1,2,1)
plt.imshow(img_intensidade,cmap="gray") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.title("Escala de Cinza")
plt.colorbar(orientation = 'horizontal')

plt.subplot(1,2,2)
plt.imshow(img_recorte,cmap="gray") # https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.title('RECORTE')
plt.colorbar(orientation = 'horizontal')
plt.show()
########################################################################################################################