# exemplo final com todos os tipos primitivos

# exemplo 1
# nome = "Joao"
# idade = 30
# saldo = 1500.75
# mensagem = f"Ola, {nome}! Você tem {idade} anos e um saldo de R${saldo:.2f}"
# print(mensagem)

# exemplo 2

# Leitura de dados
peso_txt = input("Digite seu peso (em kg): ")
altura_txt = input("Digite sua altura (em metros): ")

# conversao de tipos para float
peso = float(peso_txt)
altura = float(altura_txt)

# calculo do IMC
imc = peso / (altura ** 2)

# classificacao do IMC
sobrepeso = imc >= 25 # boolean

# saida formatada (string)
print(f"Seu IMC é: {imc:.1f}")
print(f"Está em sobrepeso? {sobrepeso}")