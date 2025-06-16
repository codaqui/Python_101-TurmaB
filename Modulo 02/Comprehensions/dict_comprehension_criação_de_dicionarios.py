# Dict Compreension - Criação de Dicionários
# Dict Comprehension é uma forma concisa de criar dicionários em Python.
# A sintaxe é semelhante à List Comprehension, mas utiliza chaves `{}` e dois pontos `:` para separar chave e valor.
# Sintaxe:
#     - {chave: valor for item in iterável if condição}
# Exemplo de Dict Comprehension:
nomes = ["ana", "bruno", "carlos"]
dicionario = {nome: len(nome) for nome in nomes}
# {'ana': 3, 'bruno': 5, 'carlos': 6}
