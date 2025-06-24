def filtra_pares(lista):
    """
    Recebe uma lista de inteiros e retorna uma nova lista contendo apenas os números pares.
    :param lista: lista de inteiros
    :return: lista de inteiros pares
    """
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return pares

valores = [1, 2, 3, 4, 5, 6]
print(filtra_pares(valores))  # [2, 4, 6]