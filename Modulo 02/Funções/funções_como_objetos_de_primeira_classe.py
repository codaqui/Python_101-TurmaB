def aplicar(func, valor):
    return func(valor)

def dobro(x):
    return x * 2

print(aplicar(dobro, 5))  # 10

# Permite programação funcional e padrões como callbacks.