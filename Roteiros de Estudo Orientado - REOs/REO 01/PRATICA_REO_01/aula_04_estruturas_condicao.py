########################################################################################################################
# DATA: 28/06/2020
# DISCIPLINA: VISÃO COMPUTACIONAL NO MELHORAMENTO DE PLANTAS
# PROFESSOR: VINÍCIUS QUINTÃO CARNEIRO
# E-MAIL: vinicius.carneiro@ufla.br
# GITHUB: vqcarneiro
########################################################################################################################
# AULA 03
# TEMA: Estrutura de condição

########################################################################################################################
#Exemplo 01: Estrutura de condição - if simples
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

print('Exemplo 01 - ESTRUTURA DE CONDIÇÃO: IF ELSE')

joao_idade = 18
print('A idade de João é: ' + str(joao_idade))

if joao_idade>=18:
    print('João pode consumir bebida alcoolica')
else:
    print('João não pode consumir bebida alcoolica')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Exemplo 01: Estrutura de condição - if simples
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
########################################################################################################################




