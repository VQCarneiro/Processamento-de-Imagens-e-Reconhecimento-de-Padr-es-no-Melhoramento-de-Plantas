########################################################################################################################
# DATA: 28/06/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro
########################################################################################################################
# AULA 05
# TEMA: Tipos complexos de dados (Coleções) - Listas, Tuplas e Dicionários

########################################################################################################################
#Exemplo 01: Listas
# Observação: Mutaveis
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exemplo 01 - Listas [] (Mutáveis)')
print('_________________________________________________________________________________________________________________')
alturas = [1.80,1.75,1.65,1.92]
alturas_backup = alturas.copy()
print('Lista Alturas: ' + str(alturas))
num_elementos = len(alturas) # Dimensão da lista
print('A lista alturas contém ' + str(num_elementos) + ' elementos')
print('As duas primeiras alturas são: ' + str(alturas[0:2]))
print('A terceira altura é: ' +str(alturas[2]))
print('Segundo elemento em diante da lista alturas: ' + str(alturas[1:]))
print('_________________________________________________________________________________________________________________')
alturas.append(1.78) # Adição de um novo valor no final da lista
print('Lista altura adicionada de um novo valor: ' + str(alturas))
print('A nova lista alturas contém ' + str(len(alturas)) + ' elementos')
print('_________________________________________________________________________________________________________________')
alturas.remove(1.65) # Remoção de um valor
print('Lista alturas removendo o valor 1.65: ' + str(alturas))
print('A nova lista alturas contém ' + str(len(alturas)) + ' elementos')
print('_________________________________________________________________________________________________________________')
alturas[1] = 1.43
print('Substituindo o segundo valor por 1.43: ' + str(alturas))
print('_________________________________________________________________________________________________________________')
alturas.reverse() # Inversão da lista
print('Lista Alturas Reversa: ' + str(alturas))
print('_________________________________________________________________________________________________________________')
alturas.sort() # Ordenamento da lista
print('Lista Alturas Ordenada: ' + str(alturas))
print('_________________________________________________________________________________________________________________')
print('Lista alturas final: ' + str(alturas))
print('Lista alturas original: ' + str(alturas_backup))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 02 - Tuplas () (Não Mutáveis')
print('-----------------------------------------------------------------------------------------------------------------')
alturas_tp = (1,2,3,4,5,6)
#alturas_tp = 1,2,3,4,5,6
print('Tupla Alturas: ' + str(alturas_tp))
print('Tipo')
print(type(alturas_tp))
print('Dimensão: ' + str(len(alturas_tp)))
print('-----------------------------------------------------------------------------------------------------------------')
#alturas_tp[2] = 4 # Erro: não aceita alteração
#alturas_tp = alturas_tp.append(1) # Erro não aceita alteração
print('-----------------------------------------------------------------------------------------------------------------')
alturas_ls = list(alturas_tp)
print('Lista Alturas: ' + str(alturas_ls))
print('Tipo')
print(type(alturas_ls))
alturas_ls[2] = 4
print('Substituição do terceiro valor: ' +str(alturas_ls))
alturas_ls.append(1)
print('Adição do valor 1 ao final da lista: ' + str(alturas_ls))
print('-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# Exemplo 03 - Dicionários
print('Exemplo 03 - Dicionários')
print('-----------------------------------------------------------------------------------------------------------------')
dic_pessoas = {'Pessoas':['João','Pedro', 'Maria'],
              'Alturas':[1.7,1.6,1.9],
              'Pesos':[79, 70, 82]}

print('Dicionário')
print(dic_pessoas)
print('-----------------------------------------------------------------------------------------------------------------')
print('Tipo')
print(type(dic_pessoas))
print('Dimensão: ' +str(len(dic_pessoas)))
print('Chaves: ' +str(dic_pessoas.keys()))
print('Valores: ' +str(dic_pessoas.values()))
print('Itens: ' +str(dic_pessoas.items()))
print('-----------------------------------------------------------------------------------------------------------------')
pessoas = dic_pessoas['Pessoas']
print('Pessoas: ' +str(pessoas))
print('-----------------------------------------------------------------------------------------------------------------')
dic_pessoas['Idades'] = [27,32,45]
print('Dicionário')
print(dic_pessoas)
print('-----------------------------------------------------------------------------------------------------------------')
'''
########################################################################################################################



