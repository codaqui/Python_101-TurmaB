"""
tupla1 = (1, 2, 3)
tupla2 = "a", "b", "c"  # parênteses são opcionais
tupla3 = ()             # tupla vazia
tupla4 = (42,)          # tupla com 1 elemento (vírgula obrigatória!)
"""

# tupla:
minha_tupla = (10, "Python", True)

# Acessando elementos da tupla
print(minha_tupla[0])  # Acessa o primeiro elemento (10)
# Tuplas são imutáveis, então não podemos alterar seus elementos

# Percorrendo a tupla
for item in minha_tupla:
    print(item)

# Iterando sobre uma tupla
for i in range(len(minha_tupla)):
    print(f"Elemento {i}: {minha_tupla[i]}")

# Bonus: Métodos úteis para tuplas

cores = ("azul", "verde", "azul", "amarelo")
print(cores.count("azul"))   # 2
print(cores.index("verde"))  # 1
