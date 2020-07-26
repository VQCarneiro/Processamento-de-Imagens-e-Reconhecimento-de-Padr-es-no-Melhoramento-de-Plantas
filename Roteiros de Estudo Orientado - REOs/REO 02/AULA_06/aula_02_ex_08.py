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
# PROCEDIMENTO: Virar imagens binárias
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

#nome_arquivo = 'feijao.jpg'
nome_arquivo = 'img_ex.jpg'
img = cv2.imread(nome_arquivo,1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print('----------------------------------------------------------------------------------------------------------------')
print('IMAGEM ORIGINAL')
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canais = np.shape(img)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Transformações em imagens - Virar
# Virar Horizontalmente
img_fp1 = cv2.flip(img,1)
print('----------------------------------------------------------------------------------------------------------------')
print('Virar Horizontalmente')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canais = np.shape(img_fp1)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))

# Virar Verticalmente
img_fp2 = cv2.flip(img,0)
print('----------------------------------------------------------------------------------------------------------------')
print('Virar Verticalmente')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canais = np.shape(img_fp2)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))

# Virar Horizontalmente e Verticalmente
img_fp3 = cv2.flip(img,-1)
print('----------------------------------------------------------------------------------------------------------------')
print('Virar Horizontalmente e Verticalmente')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col,canais = np.shape(img_fp3)
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
plt.imshow(img_fp1)
plt.title("Horizontal (H)")

plt.subplot(2,2,3)
plt.imshow(img_fp2)
plt.title("Vertical (V)")

plt.subplot(2,2,4)
plt.imshow(img_fp3)
plt.title("H e V")

plt.show()
########################################################################################################################