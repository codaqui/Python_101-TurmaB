# exemplo de uso do break:
for numero in range(10):
    if numero == 5:
        break  # para tudo aqui
    print(numero)
# Assim que numero == 5, o laço é interrompido e não imprime mais nada.

# exemplo de uso do continue:
for numero in range(10):
    if numero == 5:
        continue  # pula para a próxima iteração
    print(numero)
# O número 2 não é impresso, pois a iteração foi "pulada".