########################################################################################################################
# DATA: 03/07/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro - https://github.com/VQCarneiro
########################################################################################################################
# AULA 03
# TEMA: Estrutura de Condição
########################################################################################################################
'''
#Exemplo 01: Estrutura de condição - if simples
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Exemplo 01 - ESTRUTURA DE CONDIÇÃO: IF ELSE')

joao_idade = 18
print('A idade de João é: ' + str(joao_idade))

if joao_idade>=18:
    print('João pode consumir bebida alcoólica')
else:
    print('João não pode consumir bebida alcoólica')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
#Exemplo 02: Estrutura de condição - if complexo
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Exemplo 02 - ESTRUTURA DE CONDIÇÃO: IF ELIF ELSE')

maria_idade = input('Qual a idade de Maria? ')
print('A idade de Maria é: ' + str(maria_idade))

if int(maria_idade)<16:
    print('Maria não pode votar')

elif 16<=int(maria_idade)<18 or int(maria_idade)>=60:
    print('O voto de Maria é facultativo')

else:
    print('O voto de Maria é obrigatório')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
'''
########################################################################################################################




