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
# PROCEDIMENTO: Leitura, apresentação e salvamento de imagens coloridas
########################################################################################################################
# Importar pacotes
import cv2 # Importa o pacote opencv
import numpy as np # Importa o pacote numpy
from matplotlib import pyplot as plt # Importa o pacote matplotlib
########################################################################################################################
# Leitura da imagem
nome_arquivo = 'img_rgb.png' # Nome do arquivo a ser utilizado na análise
#nome_arquivo = 'macas.jpg' # Nome do arquivo a ser utilizado na análise

img_bgr = cv2.imread(nome_arquivo,1) # Carrega imagem colorida em BGR
img_cinza = cv2.imread(nome_arquivo,0) # Carrega imagem em escala de cinza
print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM COLORIDA')
print('----------------------------------------------------------------------------------------------------------------')
print('Canal Azul')
print(img_bgr[:,:,0])
print('Canal Verde')
print(img_bgr[:,:,1])
print('Canal Vermelho')
print(img_bgr[:,:,2])

print('----------------------------------------------------------------------------------------------------------------')
print('DADOS DA IMAGEM EM ESCALA DE CINZA')
print('----------------------------------------------------------------------------------------------------------------')
print(img_cinza)
print('----------------------------------------------------------------------------------------------------------------')
print('INFORMAÇÕES')
print('----------------------------------------------------------------------------------------------------------------')
lin, col, canais = np.shape(img_bgr)
print('Dimensão: ' + str(lin) +' x '+ str(col))
print('Largura: ' + str(col))
print('Altura: ' + str(lin))
print('Número de Canais: ' + str(canais))
print('----------------------------------------------------------------------------------------------------------------')

########################################################################################################################
# Correção do ordenamento dos canais das imagens
# Alternativa 1:
#b,g,r = cv2.split(img_bgr)
# = cv2.merge([r,g,b])

# Alternativa 2:
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
########################################################################################################################
# Apresentar imagens

# Imagem Em RGB
plt.figure('Imagem em RGB')
plt.imshow(img_rgb)
plt.title("Imagem em RGB")
plt.show()

# Todas em uma única figura
plt.figure('Imagens')
plt.subplot(221)
plt.imshow(img_rgb)
plt.title("RGB")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(222)
plt.imshow(img_bgr)
plt.title("BGR")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(223)
plt.imshow(img_cinza, cmap = 'gray')
plt.title("Escala de Cinza")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.subplot(224)
plt.imshow(img_cinza, cmap = 'jet')
plt.title("JET")
plt.xticks([]) # Eliminar o eixo X
plt.yticks([])  # #liminar o eixo y

plt.show()
########################################################################################################################
'''
# Salvar imagens
# Salvar imagem em RGB
cv2.imwrite('exemplo.png',img_bgr)
# Salvar imagem em escala de cinza
cv2.imwrite('exemplo_cinza.png',img_cinza)
'''
########################################################################################################################