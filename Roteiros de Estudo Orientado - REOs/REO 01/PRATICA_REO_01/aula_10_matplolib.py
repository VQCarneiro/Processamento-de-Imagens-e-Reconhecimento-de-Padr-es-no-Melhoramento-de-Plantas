########################################################################################################################
# DATA: 03/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# AULA 10
# TEMA: Gráficos

########################################################################################################################
#Exemplo 1: Gráficos de Dispersão
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 01: Gráfico de Dispersão')
print('-----------------------------------------------------------------------------------------------------------------')
from matplotlib import pyplot as plt
import numpy as np
import os

dados = np.loadtxt('dados_selecionados.txt')
nl, nc = dados.shape
print(dados)

#Graficos
plt.style.use('ggplot')
fig = plt.figure('Dispersão')
plt.subplot(1,2,1)
plt.scatter(dados[:,1], dados[:,2],s=50,alpha=1,c='blue')
plt.title('Dispersão')
plt.xlabel('Var X')
plt.ylabel('Var Y')


plt.subplot(1,2,2)
cores = ['black','blue','red','green','yellow','pink','cyan','orange','darkviolet','slategray']
# https://matplotlib.org/3.1.0/gallery/color/named_colors.html
for i in np.arange(0,nl,1):
    plt.scatter(dados[i,1], dados[i,2],s=50,alpha=0.8,label = dados[i,0],c = cores[i])

plt.title('Dispersão')
plt.xlabel('Var X')
plt.ylabel('Var Y')
plt.legend()
plt.show()

#Salvar grafico
#nome = 'dispersao2D'
#fig.savefig((nome+'.png'), bbox_inches="tight")
#os.startfile(nome+'.png')
'''

'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 02: Gráfico de Barra')
print('-----------------------------------------------------------------------------------------------------------------')
from matplotlib import pyplot as plt
import numpy as np

dados = np.loadtxt('dados_selecionados.txt')
nl, nc = dados.shape
print('Dados')
print(dados)

plt.figure('Variável 1')
plt.subplot(2,2,1)
plt.bar(dados[:,0],dados[:,1])
plt.title('Gráfico de Barras')
plt.xticks(dados[:,0])

plt.subplot(2,2,4)
plt.bar(dados[:,0],dados[:,2])
plt.title('Variável 2')
plt.xticks(dados[:,0])
plt.show()

print('-----------------------------------------------------------------------------------------------------------------')
'''
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 03: Gráficos')
print('-----------------------------------------------------------------------------------------------------------------')
from matplotlib import pyplot as plt
import numpy as np

np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
dados = np.loadtxt('dados_reg.txt')
nl, nc = dados.shape
print('Dados')
print(dados)

plt.style.use('seaborn-dark') # https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
plt.figure('Variável 1')

plt.subplot(3,3,1)
plt.scatter(dados[:,0],dados[:,2],c='forestgreen',s=20,alpha=0.8)
plt.title('Produtividade x Densidade')
plt.xticks(dados[:,0])
plt.yticks(range(3000,4300,200))
plt.legend()
plt.grid()

plt.subplot(3,3,3)
f = lambda x: 64.9667*x + 2865.4
rotulo = 'Y = '+ str(2865.4) +' + '+ str(64.9667) +'$^*$$^*$x; R² = ' + str(91.9) + '%'
plt.plot(dados[:,0],f(dados[:,0]),c='black', label = rotulo)
plt.title('Produtividade x Densidade')
plt.xticks(dados[:,0])
plt.yticks(range(3000,4300,200))
plt.legend()
plt.grid()


plt.subplot(3,3,5)
plt.scatter(dados[:,0],dados[:,2],c='forestgreen',s=20,alpha=0.8)
f = lambda x: 64.9667*x + 2865.4
rotulo = 'Y = '+ str(2865.4) +' + '+ str(64.9667) +'$^*$$^*$x; R² = ' + str(91.9) + '%'
plt.plot(dados[:,0],f(dados[:,0]),c='black', label = rotulo)
plt.title('Produtividade x Densidade')
plt.xticks(dados[:,0])
plt.yticks(range(3000,4300,200))
plt.legend()
plt.grid()

plt.show()
'''