# Set Comprehension – Criação de conjuntos
# Set Comprehension é uma forma concisa de criar conjuntos (sets) em Python.
# A sintaxe é semelhante à List Comprehension, mas utiliza chaves `{}` em vez de colchetes `[]`.
# Sintaxe:
#     - {expressão for item in iterável if condição}
# Exemplo de Set Comprehension
numeros = [1, 2, 3, 4, 5]
quadrados_set = {n**2 for n in numeros}
print(quadrados_set)  # {1, 4, 9, 16, 25}
# Set Comprehension com Condição

pares_set = {n for n in numeros if n % 2 == 0}
print(pares_set)  # {2, 4}

# Set Comprehension com Condição e Expressão
cubos_set = {n**3 for n in numeros if n % 2 != 0}
print(cubos_set)  # {1, 27, 125}
