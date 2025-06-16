"""
break: Interrompe o laço
continue: Pula para a próxima iteração
else: Executa quando o laço termina normalmente (sem break)
"""

for i in range(10):
    if i == 5:
        break
    print(i)

# while com else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop finalizado")
