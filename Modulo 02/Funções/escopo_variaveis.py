# Exemplo 1: variável local não afeta a global
p = 10  # variável global

def mostra_x():
    x = 5  # variável local: só existe dentro da função
    print("Dentro de mostra_x, x =", x)

mostra_x()           # imprime: Dentro de mostra_x, x = 5
print("Fora da função, x =", p)  # imprime: Fora da função, x = 10

# Exemplo 2: usando 'global' para modificar a variável global
y = 20

def altera_global():
    global y
    y = 30  # modifica a variável global y
    print("Dentro de altera_global, y =", y)

print("Antes de chamar altera_global, y =", y)  # 20
altera_global()                                # Dentro de altera_global, y = 30
print("Depois de chamar altera_global, y =", y)  # 30

# Exemplo 3: mutável sem 'global' (lista)
lista = [1, 2, 3]

def adiciona_valor(v):
    # Não precisa de 'global' para modificar o conteúdo da lista,
    # pois a referência 'lista' vem do escopo externo, mas a operação
    # altera o objeto mutável.
    lista.append(v)
    print("Dentro de adiciona_valor:", lista)

print("Antes:", lista)       # [1, 2, 3]
adiciona_valor(4)            # Dentro de adiciona_valor: [1, 2, 3, 4]
print("Depois:", lista)      # [1, 2, 3, 4]

"""
No Exemplo 1, x definido dentro de mostra_x é local e não interfere em x fora da função.

No Exemplo 2, para reatribuir a variável global dentro da função, usamos global y. Sem isso, uma atribuição criaria só uma variável local.

No Exemplo 3, lista é um objeto mutável. Mesmo sem declarar global lista, ainda podemos modificar seu conteúdo (método .append()), pois 
não reatribuímos a variável, apenas alteramos o objeto apontado pela referência.

Isso demonstra como escopos local e global se comportam em Python. Variáveis definidas dentro de funções (sem global) são isoladas; já objetos 
mutáveis referenciados externamente podem ser modificados sem reatribuição da variável global.
"""