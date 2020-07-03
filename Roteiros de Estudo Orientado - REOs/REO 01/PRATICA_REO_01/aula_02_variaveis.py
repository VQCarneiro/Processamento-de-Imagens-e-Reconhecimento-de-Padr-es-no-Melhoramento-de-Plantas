########################################################################################################################
# DATA: 28/06/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro
########################################################################################################################
# AULA 02
# TEMA: TIPOS PRIMITIVOS, DECLARAÇÃO DE VARIÁVEIS E IMPRESSÃO NO CONSOLE

########################################################################################################################
#Exemplo 01: Imprimir na tela
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exemplo 01')
print('Olá Mundo!')

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 02: Declarar variável string
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
msg = 'Olá Mundo!'
dimensao_msg = len(msg)
tipo_msg = type(msg)
print('Exemplo 02')
print('A variável msg contém: ' + msg)
print('Tipo da variável msg: ' + str(tipo_msg))
print('A variável msg possui ' + str(dimensao_msg) + ' caracteres')
letra_0 = msg[0]
print('O caractere na posição 0 é: ' + letra_0)
print('O caractere na posição 4 é: ' + msg[4])
print('O caractere na posição 9 é: ' + msg[9])
# Dica: toda variável em Python inicia na posição 0!

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 03: Declarar uma variável que contém um valor inteiro
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
valor = 5
tipo_valor = type(valor)
print('Exemplo 03')
print('A variável valor contém: ' + str(valor))
print('Tipo da variável valor: ' + str(tipo_valor))

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 04: Declarar uma variável que contém um valor decimal (float)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
valor_decimal = 30.5
tipo_valor_decimal = type(valor_decimal)
print('Exemplo 04')
print('A variável valor_decimal contém: ' + str(valor_decimal))
print('Tipo da variável valor_decimal: ' + str(tipo_valor_decimal))

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 05: Declarar uma variável booleana (Verdadeiro (True) ou Falso (False)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
v_bool = True
tipo_v_bool = type(v_bool)
print('Exemplo 05')
print('A variável v_bool contém: ' + str(v_bool))
print('Tipo da variável v_bool: ' + str(tipo_v_bool))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
########################################################################################################################




