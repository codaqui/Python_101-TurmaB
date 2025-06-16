# filtragem de elementos:
pares = [x for x in range(10) if x % 2 == 0]

# transformações simples:
palavras = ["python", "é", "massa"]
upper = [p.upper() for p in palavras]

# criação de dicionários:
quadrados = {x: x**2 for x in range(5)}

# Remoção de duplicatas
sem_repetidos = {x for x in [1, 2, 2, 3, 3, 3]}

# Geração sob demanda (grandes volumes)
gen = (x * 2 for x in range(10**6))  # usa pouca memória
