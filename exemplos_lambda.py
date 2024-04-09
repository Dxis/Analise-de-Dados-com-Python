import pandas as pd 


# Criando um DataFrame a partir de um dicionário
data = {
    'Nome':['diego','nathalia','aurora'],
    'Idade': [34,29,1],
    'Cidade':['diadema','diadema','diadema']
}

df = pd.DataFrame(data)


# Adiciona 2 a x
df['Idade_Adicionada'] = df['Idade'].apply(lambda x: x + 2)

# Eleva x ao quadrado
df['Idade_Quadrada'] = df['Idade'].apply(lambda x: x ** 2)

# Converte s para maiúsculas
df['Nome_Maiusculo'] = df['Nome'].apply(lambda xs: xs.upper())

# Substitui 'a' por 'b' em s
df['Cidade_ok'] = df['Cidade'].apply(lambda s: s.replace('diadema', 'Diadema'))

# Verifica se x é par
df['Paridade'] = df['Idade'].apply(lambda x: 'Par' if x % 2 == 0 else 'Ímpar')

# Verifica se 'a' está em s
df['Contem_h'] = df['Nome'].apply(lambda s: 'Sim' if 'h' in s else 'Não')

# Definindo a função my_function
def my_function(value):
    # Exemplo simples: retorna o valor multiplicado por 2
    return value * (-1)

# Chama a função my_function com argumento x
df['my_function'] = df['Idade'].apply(lambda x: my_function(x))

# Retorna o comprimento de uma lista lst
df['Tamanho_Lista'] = df['Nome'].apply(lambda labcst: len(labcst))

print(df)

# Ordena os valores da coluna 'Idade' em ordem decrescente
df_sorted = df.sort_values(by='Idade', ascending=True)

print(df_sorted)

# Aplicando a função map() para adicionar 10 anos à idade de cada pessoa
df['Idade_Adicionada'] = df['Idade'].map(lambda x: x + 10)

print("DataFrame com 10 anos adicionados à idade:")
print(df)

# Usando a função filter() para filtrar apenas as idades maiores que 20
df_filtrado = df[df['Idade'].apply(lambda x: x > 20)]

print("\nDataFrame com apenas idades maiores que 20:")
print(df_filtrado)