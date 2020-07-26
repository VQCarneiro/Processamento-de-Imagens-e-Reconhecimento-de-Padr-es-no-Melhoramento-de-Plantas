########################################################################################################################
# Lavras - MG
# 21/04/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Processamento de imagens e reconhecimento de padrões no melhoramento de plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# Github: vqcarneiro
########################################################################################################################
# PROCEDIMENTO: Recortar imagens coloridas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img = cv2.imread(nome_arquivo,1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print('----------------------------------------------------------------------------------------------------------------')
print('IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin_or, col_or, canais_or = np.shape(img)
print('Dimensão: ' + str(lin_or) +' x '+ str(col_or))
print('Largura: ' + str(col_or))
print('Altura: ' + str(lin_or))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Transformações em imagens - Virar
# Recorte 1

img_rc1 = img[0:int(lin_or/2),0:int(col_or/2)]
print('----------------------------------------------------------------------------------------------------------------')
print('Recorte 1 = 0:Metade,0:Metade')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais  = np.shape(img_rc1)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))

# Recorte 2
img_rc2 = img[150:1450,470:1700]
print('----------------------------------------------------------------------------------------------------------------')
print('Recorte 2 = Área útil')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais = np.shape(img_rc2)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))

# Recorte 3
img_rc3 = img[800:1000,0::]
print('----------------------------------------------------------------------------------------------------------------')
print('Recorte 3 = 800:1000,0::')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canais = np.shape(img_rc3)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('VIRAR')
plt.subplot(2,2,1)
plt.imshow(img)
plt.title("ORIGINAL")


plt.subplot(2,2,2)
plt.imshow(img_rc1)
plt.title("Recorte 1")

plt.subplot(2,2,3)
plt.imshow(img_rc2)
plt.title("Recorte 2")

plt.subplot(2,2,4)
plt.imshow(img_rc3)
plt.title("Recorte 3")

plt.show()
########################################################################################################################