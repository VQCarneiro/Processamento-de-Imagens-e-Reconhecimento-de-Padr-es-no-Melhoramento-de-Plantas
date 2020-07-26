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
# PROCEDIMENTO: Redimensionar imagens binárias
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem
nome_arquivo = 'img_quadrado.png'
img = cv2.imread(nome_arquivo,0)
########################################################################################################################
# Transformações em imagens - Redimensionar

dim = (5000,5000)
img_rr1 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

dim = (5000,1000)
img_rr2 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

# Redimensionar por um número de colunas específico
r = 5/img.shape[1] # Razão de proporção
dim = (5,int(img.shape[0]*r))
img_rr3 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA) # Verificar outros métodos de interpolação

# Redimensionar por um número de linhas específico
r = 300/img.shape[0]
dim = (int(img.shape[1]*r),300)
img_rr4 = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('REDIMENSIONAR')
plt.subplot(1,5,1)
plt.imshow(img,cmap="gray")
plt.title("ORIGINAL")

plt.subplot(1,5,2)
plt.imshow(img_rr1,cmap="gray")
plt.title("5000x5000")

plt.subplot(1,5,3)
plt.imshow(img_rr2,cmap="gray")
plt.title("1000X5000")

plt.subplot(1,5,4)
plt.imshow(img_rr3,cmap="gray")
plt.title("5X5")

plt.subplot(1,5,5)
plt.imshow(img_rr4,cmap="gray")
plt.title("300x300")

plt.show()
########################################################################################################################