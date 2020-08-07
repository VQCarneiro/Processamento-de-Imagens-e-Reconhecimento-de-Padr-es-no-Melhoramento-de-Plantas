########################################################################################################################
# Lavras - MG
# 02/08/2020
# Universidade Federal de Lavras - UFLA
# Departamento de Biologia
# Programa de Pós Graduação em Genética e Melhoramento de Plantas
# Disciplina: Visão Computacional No Melhoramento de Plantas
# Docente: Vinícius Quintão Carneiro
# E-mail: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# PROCEDIMENTO: Tipos de Filtros
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem

nome_arquivo = 'feijao.jpg'
img_bgr = cv2.imread(nome_arquivo,1)
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
########################################################################################################################
# Filtros
# Média
img_filtro_media = cv2.blur(img_rgb,(51,51))

img_filtro_gaussiano = cv2.GaussianBlur(img_rgb,(51,51),0) # Média Ponderada

img_filtro_mediana = cv2.medianBlur(img_rgb,51)

img_filtro_bilateral = cv2.bilateralFilter(img_rgb,51,51,21)
########################################################################################################################
# Apresentar imagens no matplotlib
plt.figure('Filtro Média')
plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("ORIGINAL")

plt.subplot(2,3,2)
plt.imshow(img_filtro_media)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("Média")

plt.subplot(2,3,3)
plt.imshow(img_filtro_gaussiano)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("Gaussiano")

plt.subplot(2,3,4)
plt.imshow(img_filtro_mediana)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("Mediana")

plt.subplot(2,3,5)
plt.imshow(img_filtro_bilateral)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("Bilateral")

plt.show()
########################################################################################################################



