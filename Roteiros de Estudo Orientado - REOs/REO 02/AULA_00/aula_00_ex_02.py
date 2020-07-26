# ########################################################################################################################
# # Lavras - MG
# # 13/07/2020
# # Universidade Federal de Lavras - UFLA
# # Departamento de Biologia
# # Programa de Pós Graduação em Genética e Melhoramento de Plantas
# # Disciplina: Visão Computacional No Melhoramento de Plantas
# # Professor: Vinícius Quintão Carneiro
# # E-mail: vinicius.carneiro@ufla.br
# # GITHUB: vqcarneiro - https://github.com/VQCarneiro
# ########################################################################################################################
# # PROCEDIMENTO: Modificações nos Valores de Uma Imagem
# ########################################################################################################################
# # Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
# ########################################################################################################################
# # Leitura da imagem
nome_arquivo = "img_quadrado.png" # Nome do arquivo a ser utilizado na análise
img_bin = cv2.imread(nome_arquivo,0) # Carrega imagem (0 - Binária e Escala de Cinza; 1 - Colorida (BGR))
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
print(img_bin)
print('----------------------------------------------------------------------------------------------------------------')
# ########################################################################################################################
# # Modificação de valores de pixels individuais
img_mod_01=np.copy(img_bin)
img_mod_01[5,5] = 255
img_mod_01[5,1] = 0
#
#
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM MODIFICADA 01 - PIXEL INDIVIDUAL')
print('----------------------------------------------------------------------------------------------------------------')
print(img_mod_01)
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
valor_pixel_00 = img_mod_01[5,5]
print("Valor do pixel da imagem modificada 01 na posição (5,5): " + str(valor_pixel_00))
valor_pixel_51 = img_mod_01[5,1]
print("Valor do pixel da imagem modificada 01 na posição (5,1): " + str(valor_pixel_51))
print('----------------------------------------------------------------------------------------------------------------')
# ########################################################################################################################
# # Modificação de valores de regiões de pixels
img_mod_02 = np.copy(img_bin)
img_mod_02[0:6,0:6] = 0
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
print(img_bin)
print('----------------------------------------------------------------------------------------------------------------')
#
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM MODIFICADA 02 - REGIÃO DE PIXELS')
print('----------------------------------------------------------------------------------------------------------------')
print(img_mod_02)
print('----------------------------------------------------------------------------------------------------------------')
# ########################################################################################################################
# # Imagem
#
plt.figure('Imagens')
plt.subplot(1,3,1)
plt.imshow(img_bin,cmap="gray")
plt.title("ORIGINAL")
plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,10,1))

plt.subplot(1,3,2)
plt.imshow(img_mod_01,cmap="gray")
plt.title("Pixel")
plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,10,1))
#
plt.subplot(1,3,3)
plt.imshow(img_mod_02,cmap="gray")
plt.title("Região")
plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,10,1))
plt.show()
# ########################################################################################################################
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
