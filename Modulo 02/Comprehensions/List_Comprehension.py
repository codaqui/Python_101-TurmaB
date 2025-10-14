"""
sintaxe:
    - [expressão for item in iterável if condição]
"""

# Exemplo de List Comprehension
numeros = [1, 2, 3, 4, 5]
quadrados = [n**2 for n in numeros]
print(quadrados)  # [1, 4, 9, 16, 25]

# List Comprehension com Condição
pares = [n for n in numeros if n % 2 == 0]
#       [expressão for item in iterável if condição]
print(pares)  # [2, 4]
