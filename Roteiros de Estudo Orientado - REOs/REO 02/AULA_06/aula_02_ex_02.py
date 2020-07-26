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
# PROCEDIMENTO: Redimensionar imagens coloridas
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
lin, col,canais = np.shape(img)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print("Canais: " + str(canais))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Transformações em imagens - Redimensionar
# Redimensionar por um número de colunas específico
r = 100/img.shape[1] # Razão de proporção
dim = (100,int(img.shape[0]*r))
img_rr1 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA) # Verificar outros métodos de interpolação
print('----------------------------------------------------------------------------------------------------------------')
print("NOVA DIMENSÃO" + str(img_rr1.shape[:2]))
print('----------------------------------------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_rr1)[:2]
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Razão de proporção: ' + str(r))

# Redimensionar por um número de linhas específico
r = 300/img.shape[0]
dim = (int(img.shape[1]*r),300)
img_rr2 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('----------------------------------------------------------------------------------------------------------------')
print("NOVA DIMENSÃO" + str(img_rr2.shape[:2]))
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_rr2)[:2]
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Razão de proporção: ' + str(r))

r = 500/img.shape[0]
dim = (int(img.shape[1]*r),500)
img_rr3 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('----------------------------------------------------------------------------------------------------------------')
print("NOVA DIMENSÃO" + str(img_rr3.shape[:2]))
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_rr3)[:2]
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))

dim = (img.shape[1]*3,img.shape[0]*3)
img_rr4 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
#img_rr4 = transformacoes.redimensionar(img,img.shape[1]*3,img.shape[0]*3)
print('----------------------------------------------------------------------------------------------------------------')
print("NOVA DIMENSÃO" + str(img_rr4.shape[:2]))
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_rr4)[:2]
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))

dim = (int(img.shape[1]/100),int(img.shape[0]/100))
img_rr5 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('----------------------------------------------------------------------------------------------------------------')
print("NOVA DIMENSÃO" + str(img_rr5.shape[:2]))
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col = np.shape(img_rr5)[:2]
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('----------------------------------------------------------------------------------------------------------------')
########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('TRANSLAÇÃO')
plt.subplot(2,3,1)
plt.imshow(img,cmap="gray")
plt.title("ORIGINAL")


plt.subplot(2,3,2)
plt.imshow(img_rr1,cmap="gray")
plt.title(str(img_rr1.shape[0]) + "X" + str(img_rr1.shape[1]))

plt.subplot(2,3,3)
plt.imshow(img_rr2,cmap="gray")
plt.title(str(img_rr2.shape[0]) + "X" + str(img_rr2.shape[1]))

plt.subplot(2,3,4)
plt.imshow(img_rr3,cmap="gray")
plt.title(str(img_rr3.shape[0]) + "X" + str(img_rr3.shape[1]))

plt.subplot(2,3,5)
plt.imshow(img_rr4,cmap="gray")
plt.title(str(img_rr4.shape[0]) + "X" + str(img_rr4.shape[1]))

plt.subplot(2,3,6)
plt.imshow(img_rr5,cmap="gray")
plt.title(str(img_rr5.shape[0]) + "X" + str(img_rr5.shape[1]))

plt.show()
########################################################################################################################