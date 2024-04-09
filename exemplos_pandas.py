import pandas as pd 

# Criando um DataFrame a partir de um dicionário
data = {
    'Nome':['diego','nathalia','aurora'],
    'Idade': [34,29,1],
    'Cidade':['diadema','diadema','diadema']
}

df = pd.DataFrame(data)
print(df)

# Criando uma tupla
'''
Uma tupla em Python é uma coleção ordenada e imutável de elementos. 
Ela é semelhante a uma lista, mas com a diferença fundamental de que uma vez que uma tupla é criada,
seus elementos não podem ser alterados, adicionados ou removidos. 
'''
tupla = (1, 'abc', True)
print("Tupla:")
print(tupla)

# Criando uma lista
lista = [1, 2, 3, 4, 5]
print("Lista:")
print(lista)

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
print("Dicionário:")
print(dicionario)

# Criando um conjunto
conjunto = {1, 2, 3, 4, 5}
print("Conjunto:")
print(conjunto)

#criando variavel a partir do data frame
idade = df['Idade']

#criando variavel a partir do data frame - duas colunas 
subset = df[['Nome','Idade']]

#Filtrando linhas do DataFrame e criando uma nova variável com apenas algumas colunas:
pessoas_jovens = df[df['Idade'] <= 30][['Nome', 'Idade']]

print(idade)
print(subset)
print( 'A pessoas jovens são:',pessoas_jovens)
print(df)



