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
# PROCEDIMENTO: Filtro média
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
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
img_fm_1 = cv2.blur(img_rgb,(11,11))

img_fm_2 = cv2.blur(img_rgb,(21,21))

img_fm_3 = cv2.blur(img_rgb,(31,31))

########################################################################################################################
# Apresentar imagens no matplotlib
plt.figure('Filtros')
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("ORIGINAL")

plt.subplot(2,2,2)
plt.imshow(img_fm_1)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("11x11")

plt.subplot(2,2,3)
plt.imshow(img_fm_2)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("21x21")

plt.subplot(2,2,4)
plt.imshow(img_fm_3)
plt.xticks([]) # Eliminar o eixo X
plt.yticks([]) # Eliminar o eixo Y
plt.title("31x31")

plt.show()
########################################################################################################################



