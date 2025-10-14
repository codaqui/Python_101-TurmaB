# Comprehension que gera valores sob demanda
# Parecida com list comprehension, mas com parênteses em vez de colchetes:
# Sintaxe:
#     - (expressão for item in iterável if condição)
# Exemplo de Generator Expression
numeros = [1, 2, 3, 4, 5]
quadrados_gen = (n**2 for n in numeros)
print(quadrados_gen)  # <generator object <genexpr> at 0x...>
# Para obter os valores, é necessário iterar sobre o gerador
for quadrado in quadrados_gen:
# - (expressão for item in iterável if condição)
    print(quadrado)  # 1, 4, 9, 16, 25

#Muito útil para trabalhar com grandes volumes de dados, pois não ocupa memória criando a lista inteira.
