import numpy as np

# Criando um array unidimensional
arr1d = np.array([1, 2, 3, 4, 5])
print("Array unidimensional:")
print(arr1d)

# Criando um array bidimensional (matriz)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArray bidimensional:")
print(arr2d)

# Adição de dois arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
soma = arr1 + arr2
print("\nSoma dos arrays:")
print(soma)

# Multiplicação de um array por um escalar
arr3 = np.array([1, 2, 3])
escalar = 2
multiplicacao = escalar * arr3
print("\nMultiplicação do array por um escalar:")
print(multiplicacao)


# Calculando a média de um array
arr = np.array([1, 2, 3, 4, 5])
media = np.mean(arr)
print("\nMédia do array:")
print(media)

# Calculando o desvio padrão de um array
desvio_padrao = np.std(arr)
print("\nDesvio padrão do array:")
print(desvio_padrao)


# Acessando um elemento específico de um array
elemento = arr[2]
print("\nElemento de índice 2:")
print(elemento)

# Fatiando um array
parte_arr = arr[1:4]
print("\nParte do array:")
print(parte_arr)
