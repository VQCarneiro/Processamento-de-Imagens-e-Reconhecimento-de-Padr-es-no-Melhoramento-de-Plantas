########################################################################################################################
# DATA: 03/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# AULA 07
# TEMA: Biblioteca Numpy
########################################################################################################################
'''
#Exemplo 01: Array Numpy
# Importação da biblioteca
import numpy as np
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exemplo 01 - Lista e Array')
print('-----------------------------------------------------------------------------------------------------------------')
# Diferença entre lista e array
lista = [1,2,3]
print('Lista: ' +str(lista))
print('Tipo')
print(type(lista))
vetor = np.array(lista)
print('Vetor: ' + str(vetor))
print('Tipo')
print(type(vetor))
print('-----------------------------------------------------------------------------------------------------------------')
'''
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 02 - Array')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
# Declarando um vetor
vetor_np = np.array([10, 50, 30, 25, 100, 90, 15])
print('-----------------------------------------------------------------------------------------------------------------')

# Obtendo a dimensão de um vetor
print('Vetor: ' + str(vetor_np))
dim_01 = len(vetor_np)
print('Dimensão (dim_01): ' + str(dim_01))
print('Tipo dim_01')
print(type(dim_01))
print('-----------------------------------------------------------------------------------------------------------------')
dim_02 = np.shape(vetor_np)
tipo_dim_02 = type(dim_02)
print('Dimensão (dim_02): ' + str(dim_02))
print('Tipo dim_0')
print(type(dim_02))
print('-----------------------------------------------------------------------------------------------------------------')
dim_03 = vetor_np.shape
print('Dimensão (dim_03): ' + str(dim_03))
print('Dimensão (dim_03): ' + str(dim_03[0]))
print('-----------------------------------------------------------------------------------------------------------------')

# Acessando o valor de um vetor
print('-----------------------------------------------------------------------------------------------------------------')
print('Vetor: ' + str(vetor_np))
print('-----------------------------------------------------------------------------------------------------------------')
terceiro_valor = vetor_np[2] # Lembrar que a posição dos valores no vetor inicia em 0.
print('Vetor: ' + str(vetor_np))
print('Terceiro valor no vetor: ' + str(terceiro_valor))
pos_terceiro_valor = np.where(vetor_np==terceiro_valor)
print('Posição do valor ' + str(terceiro_valor) + ' é: ' + str(pos_terceiro_valor[0][0]))
print('-----------------------------------------------------------------------------------------------------------------')
vetor_terceiro_valor_em_diante = vetor_np[2:]
print('Vetor: ' + str(vetor_np))
print('Vetor do terceiro valor em diante: ' + str(vetor_terceiro_valor_em_diante))
print('-----------------------------------------------------------------------------------------------------------------')
vetor_terceiro_ao_quinto = vetor_np[2:5]
print('Vetor: ' + str(vetor_np))
print('Vetor do terceiro ao quinto valor: ' + str(vetor_terceiro_ao_quinto))
print('-----------------------------------------------------------------------------------------------------------------')
vetor_primeiro_ao_terceiro = vetor_np[0:3]
print('Vetor: ' + str(vetor_np))
print('Vetor do primeiro ao terceiro valor: ' + str(vetor_primeiro_ao_terceiro))
print('-----------------------------------------------------------------------------------------------------------------')
bool_menor_50 = vetor_np<50
print('Vetor: ' + str(vetor_np))
print('Vetor booleano menor que 50: ' + str(bool_menor_50))
vetor_menor_50 = vetor_np[bool_menor_50]
print('Vetor com valores menores que 50: ' + str(vetor_menor_50))
pos_menor_50 = np.where(vetor_np<50)
print('Posições com valores menores que 50: ' + str(pos_menor_50[0]))
print('-----------------------------------------------------------------------------------------------------------------')
vetor_novo_add_25 = np.append(vetor_np,25)
print('Vetor: ' + str(vetor_np))
print('Dimensão Vetor: ' + str(len(vetor_np)))
print('Novo Vetor Adição: ' + str(vetor_novo_add_25))
print('Dimensão Vetor Novo Adição: ' + str(len(vetor_novo_add_25)))
vetor_rm = np.delete(vetor_np, 2) # 2 é a posição
print('Novo Vetor Remoção: '+str(vetor_rm))
print('Dimensão Vetor Novo Remoção: ' + str(len(vetor_rm)))
print('-----------------------------------------------------------------------------------------------------------------')
print('Vetor: ' + str(vetor_novo_add_25))
valores,contagens = np.unique(vetor_novo_add_25,return_counts=True)
print('Valores Diferentes: ' + str(valores))
print('Contagem de Valores: ' + str(contagens))
print('-----------------------------------------------------------------------------------------------------------------')
'''
'''
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 03 - Array Multidimensional - Matriz')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
# Declarando uma matriz
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Matriz')
print(matriz)
print('-----------------------------------------------------------------------------------------------------------------')

# Obtendo a dimensão de uma matriz
nl,nc = np.shape(matriz)
print('Número de linhas: ' + str(nl))
print('Número de colunas: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')

# Manipulando os dados de uma matriz
print('-----------------------------------------------------------------------------------------------------------------')
vetor_lin_1 = matriz[0,:]
print('Matriz')
print(matriz)
print('')
print('Primeira linha: ' + str(vetor_lin_1))
print('-----------------------------------------------------------------------------------------------------------------')
vetor_col_fim = matriz[:,-1]
print('Matriz')
print(matriz)
print('')
print('Ultima coluna: ' + str(vetor_col_fim))
print('-----------------------------------------------------------------------------------------------------------------')
sub_matriz = matriz[1:,1:]
print('Matriz')
print(matriz)
print('')
print('Submatriz - matriz[1:,1:]')
print(sub_matriz)
print('-----------------------------------------------------------------------------------------------------------------')
sub_matriz = matriz[0:2,1:]
print('Matriz')
print(matriz)
print('')
print('Submatriz - matriz[0:2,1:]')
print(sub_matriz)
print('-----------------------------------------------------------------------------------------------------------------')
sub_matriz = matriz[[0,2],[0,2]]
print('Matriz')
print(matriz)
print('')
print('Submatriz - matriz[[0,2],[0,2]]')
print(sub_matriz)
print('-----------------------------------------------------------------------------------------------------------------')
print('Matriz')
print(matriz)
print('')
print('Valores Iguais ou Maiores que 5')
valores_iguais_maiores_5 = matriz[matriz>=5]
print(valores_iguais_maiores_5)
print('-----------------------------------------------------------------------------------------------------------------')
# Medidas de posição e dispersão
print('Matriz')
print(matriz)
print('')
print('Valores Iguais ou Maiores que 3 e Menores que 7')
valores_entre_3_7 = matriz[(matriz<7) & (matriz>3)]
print(valores_entre_3_7)
print('Posições com Valores Iguais ou Maiores que 3 e Menores que 7')
lin_entre_3_7,col_entre_3_7 = np.where((matriz<7) & (matriz>3))
print('Linha: ' + str(lin_entre_3_7))
print('Coluna: ' + str(col_entre_3_7))
print('Valores Iguais ou Maiores que 3 e Menores que 7')
print(matriz[lin_entre_3_7,col_entre_3_7])
print('-----------------------------------------------------------------------------------------------------------------')
print('Matriz')
print(matriz)
print('')

minimo = np.min(matriz)
print('Mínimo Total: '+ str(minimo))
min_lin = np.min(matriz,axis=1)
print('Mínimo Linhas: '+ str(min_lin))
min_col = np.min(matriz,axis=0)
print('Mínimo Colunas: '+ str(min_col))

maximo = np.max(matriz)
print('Máximo Total: '+ str(maximo))
max_lin = np.max(matriz,axis=1)
print('Máximo Linhas: '+ str(max_lin))
max_col = np.max(matriz,axis=0)
print('Máximo Colunas: '+ str(max_col))

media = np.mean(matriz)
print('Média Total: '+ str(media))
medias_lin = np.mean(matriz,axis=1)
print('Média Linhas: '+ str(medias_lin))
medias_col = np.mean(matriz,axis=0)
print('Média Colunas: '+ str(medias_col))

variancia = np.var(matriz)
print('Variância Populacional: '+ str(variancia))
var_lin = np.var(matriz,axis=1)
print('Variancia Linhas: '+ str(var_lin))
var_col = np.var(matriz,axis=0)
print('Variancia Colunas: '+ str(var_col))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 04 - Operações Matriciais')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
matriz_01 = np.array([[1,2],
                   [3,4],
                   [5,6],
                   [7,8],
                   [9,10],
                   [11,12],
                   [13,14],
                   [15,16]])
print('Matriz 01 (8x2)')
print(matriz_01)
print('')
nl_01,nc_01 = np.shape(matriz_01)
print('Linhas: ' + str(nl_01))
print('Colunas: ' + str(nc_01))
print('')

matriz_02 = np.array([[10,20,500],
                   [30,40,500],
                   [50,60,500],
                   [70,80,500],
                   [90,100,500],
                   [110,120,500],
                   [130,140,500],
                   [150,160,500]])
print('Matriz (8x2)')
print(matriz_02)
print('')
nl_02,nc_02 = np.shape(matriz_02)
print('Linhas: ' + str(nl_02))
print('Colunas: ' + str(nc_02))
print('')

# Concatenar matrizes
matriz_concat = np.concatenate((matriz_01,matriz_02),axis=1)
print('Matriz Concatenada')
print(matriz_concat)
print('-----------------------------------------------------------------------------------------------------------------')
print('Matriz 01 (8x2)')
print(matriz_01)
print('')

matriz_01_ref = np.reshape(matriz_01,(4,4))
print('Matriz (4x4)')
print(matriz_01_ref)
print('-----------------------------------------------------------------------------------------------------------------')
# Multiplicação de matrizes
matriz_01 = np.array([[1,2],
                   [3,4],
                   [5,6],
                   [7,8],
                   [9,10],
                   [11,12],
                   [13,14],
                   [15,16]])
print('Matriz 01 (8x2)')
print(matriz_01)
print('')
nl_01,nc_01 = np.shape(matriz_01)
print('Linhas: ' + str(nl_01))
print('Colunas: ' + str(nc_01))
print('')

matriz_02 = np.array([[10,20,500],
                   [30,40,500],
                   [50,60,500],
                   [70,80,500],
                   [90,100,500],
                   [110,120,500],
                   [130,140,500],
                   [150,160,500]])
print('Matriz (8x3)')
print(matriz_02)
print('')
nl_02,nc_02 = np.shape(matriz_02)
print('Linhas: ' + str(nl_02))
print('Colunas: ' + str(nc_02))
print('')

matriz_03 = np.reshape(matriz_02,(3,8))
print('Matriz Reformatada (3x8)')
print(matriz_03)
mult_mat = np.dot(matriz_03,matriz_01)
print('')
print('Matriz (8x2)')
print(matriz_01)
print('')
print('Multiplicação de Matrizes')
print(mult_mat)
print('-----------------------------------------------------------------------------------------------------------------')

# Inversa de Matrizes
matriz = np.array([[2,1],[5,3]])
print('Matriz')
print(matriz)
print('')
matriz_inversa = np.linalg.inv(matriz)
print('Matriz Inversa')
print(matriz_inversa)
print('')
matriz_identidade = matriz_inversa.dot(matriz)
print('Matriz Identidade')
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
print(matriz_identidade)
print('-----------------------------------------------------------------------------------------------------------------')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 05 - Criação Automática de Matrizes e Vetores')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np
matriz_uns = np.ones((10,10))
print('Matriz de uns (10x10)')
print(matriz_uns)
print('-----------------------------------------------------------------------------------------------------------------')
matriz_zeros = np.zeros((10,10))
print('Matriz de zeros (10x10)')
print(matriz_zeros)
print('-----------------------------------------------------------------------------------------------------------------')
matriz_identidade = np.eye(10)
print('Matriz identidade (10x10)')
print(matriz_identidade)
print('-----------------------------------------------------------------------------------------------------------------')
sequencia = range(0,100,20)
print('REANGE: Sequencia 0 até 100 (passo: 20)')
print(sequencia)
print('Tipo')
print(type(sequencia))
sequencia = np.array(sequencia)
print('NUMPY: Sequencia 0 até 100 (passo: 20)')
print(sequencia)
print('Tipo')
print(type(sequencia))
print('-----------------------------------------------------------------------------------------------------------------')
sequencia = np.arange(0,100,20)
print('ARANGE:Sequencia 0 até 100 (passo: 20)')
print(sequencia)
print('Tipo')
print(type(sequencia))
print('-----------------------------------------------------------------------------------------------------------------')
sequencia = np.arange(0,10,1)
print('Sequencia 0 até 9 (passo: 1)')
print(sequencia)
print('-----------------------------------------------------------------------------------------------------------------')
sequencia_02 = np.copy(sequencia)
print('Sequencia 0 até 9 (passo: 1) - copiada')
print(sequencia_02)
print('-----------------------------------------------------------------------------------------------------------------')
matriz = np.array([[1,2],[3,4]])
print('Matriz Original')
print(matriz)
matriz_backup = matriz.copy()
print('Matriz Backup')
print(matriz_backup)
print('-----------------------------------------------------------------------------------------------------------------')
'''
'''
print('-----------------------------------------------------------------------------------------------------------------')
print('Exemplo 06 - Leitura de dados txt')
print('-----------------------------------------------------------------------------------------------------------------')
import numpy as np

np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

dados = np.loadtxt('dados_medias.txt')
print('Dados')
print(dados)
nl,nc = dados.shape
print('-----------------------------------------------------------------------------------------------------------------')
print('Número de Linhas: ' + str(nl))
print('Número de Colunas: ' + str(nc))
print('-----------------------------------------------------------------------------------------------------------------')
dados_sel = dados[:,[0,3,-1]]
print('Dados Selecionados')
print('-----------------------------------------------------------------------------------------------------------------')
print(dados_sel)
print('-----------------------------------------------------------------------------------------------------------------')
#np.savetxt('dados_selecionados.txt', dados_sel, delimiter='\t', fmt='%2.4f')
import os
np.savetxt('dados_selecionados.txt', dados_sel, delimiter=' ',newline= os.linesep, fmt='%i %2.4f %2.4f')
'''

########################################################################################################################

