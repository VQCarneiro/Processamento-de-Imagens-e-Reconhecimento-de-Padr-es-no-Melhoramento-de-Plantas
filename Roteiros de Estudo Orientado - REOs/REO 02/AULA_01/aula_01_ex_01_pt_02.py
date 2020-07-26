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
# PROCEDIMENTO: Imagens Coloridas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem
#nome_arquivo = 'img_rgb.png' # Nome do arquivo a ser utilizado na análise
nome_arquivo = 'macas.jpg' # Nome do arquivo a ser utilizado na análise
img_bgr = cv2.imread(nome_arquivo,1) # Carrega imagem colorida em BGR
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
r,g,b = cv2.split(img_rgb)
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM COLORIDA')
print('----------------------------------------------------------------------------------------------------------------')
print('Canal Vermelho (R)')
print(r)
print('Canal Verde (G)')
print(g)
print('Canal Azul (B)')
print(b)
########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('Imagem')
plt.subplot(2,3,2)
plt.imshow(img_rgb)
plt.title("RGB")

plt.subplot(2,3,4)
plt.imshow(r, cmap = 'gray')
plt.title("R")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(2,3,5)
plt.imshow(g, cmap = 'gray')
plt.title("G")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(2,3,6)
plt.imshow(b, cmap = 'gray')
plt.title("B")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.show()
########################################################################################################################