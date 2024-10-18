#Listas em python

#Para fazer uma tupla se usa parênteses '()'. Tuplas são imutáveis (ex.: Meses do ano, dias da semana etc...)
#Para uma lista se usa chaves '[]'. Listas são mutáveis, é possível alterar qualquer valor dentro de uma lista, assim como
# adicionar ou retirar valores de dentro lista.

#Comandos

##ADICIONANDO VALORES A UMA LISTA##
#O comando .append('x') adiciona um valor ao final da lista
#O comando .insert(posição_na_lista, 'x') adiciona um valor em qualquer posição na lista, trazendo todos os elementos subsequentes
#para frente

##DELETANDO VALORES DE UMA LISTA##
# 1. del variável[3] - 
# 2. variavel.pop[3] - Caso não coloque um valor para remover '()' o .pop remove o ultimo item da lista
# 3. lista.remove ['x'] - Remove pelo nome do valor, não pela posição na lista.

valores = ['2', '3', '8', '9'] #Cria uma lista

def ex_list():
    valores = list(range(4,11))
    print(valores)
    pass

def ex_organizar():
    valores = ['1','4','6','3','7','9'] #cria a lista
    valores.sort() #organiza os valores
    valores.sort(reverse=True) #organiza os valores na ordem reversa
    pass

len(valores) 