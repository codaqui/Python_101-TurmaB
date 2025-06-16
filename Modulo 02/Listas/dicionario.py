# exemplo de dict:

aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Python"
}

# acessando valores
print(aluno["nome"])     # Maria
print(aluno.get("curso"))  # Python
print(aluno.get("nota", "Não existe"))  # retorna valor padrão se não encontrar

"""
principais métodos de dictionary:

| Método        | O que faz                               | Exemplo                   |
| ------------- | --------------------------------------- | ------------------------- |
| `.get(chave)` | Retorna valor da chave (ou None/padrão) | `d.get("nome")`           |
| `.keys()`     | Retorna todas as chaves                 | `d.keys()`                |
| `.values()`   | Retorna todos os valores                | `d.values()`              |
| `.items()`    | Retorna todos os pares (chave, valor)   | `d.items()`               |
| `.update()`   | Atualiza/adiciona pares chave\:valor    | `d.update({"idade": 25})` |
| `.pop(chave)` | Remove e retorna o valor da chave       | `d.pop("curso")`          |
| `.clear()`    | Limpa o dicionário                      | `d.clear()`               |
"""
# modificando valores
aluno["idade"] = 21
aluno["nota"] = 9.5  # adiciona nova chave

# removendo dados
del aluno["curso"]
aluno.pop("idade")

# Iterando sobre dicionários
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
