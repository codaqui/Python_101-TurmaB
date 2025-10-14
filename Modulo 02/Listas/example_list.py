# Exemplo de lista em Python:
minha_lista = [1, 2, 3, "Python", True]


# Acessando elementos da lista
print(minha_lista[0])  # Acessa o primeiro elemento (1)

# alterarando um elemento da lista
minha_lista[1] = 10  # Altera o segundo elemento para 10

# percorrendo a lista
for item in minha_lista:
    print(item)

"""
Métodos uteis para listas:
| Método     | O que faz                              | Exemplo                       |
| ---------- | -------------------------------------- | ----------------------------- |
| `append()` | Adiciona um item no final              | `frutas.append("melão")`      |
| `insert()` | Insere em uma posição específica       | `frutas.insert(1, "abacaxi")` |
| `remove()` | Remove a primeira ocorrência           | `frutas.remove("uva")`        |
| `pop()`    | Remove e retorna um item (por índice)  | `frutas.pop(0)`               |
| `len()`    | Retorna o tamanho da lista             | `len(frutas)`                 |
| `sort()`   | Ordena a lista **(modifica original)** em ordem alfabetica | `frutas.sort()`               |
| `sorted()` | Ordena **sem modificar original**      | `nova = sorted(frutas)`       |
"""