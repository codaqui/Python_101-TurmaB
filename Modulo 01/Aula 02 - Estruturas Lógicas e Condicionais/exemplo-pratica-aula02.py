""""
Exemplo de Classificacao de uma pessoa


pede a idade da pessoa
pergunta se ela e estudante
pergunta se ela tem cnh
classifica a pessoa em categorias usando if, elif, else e os operadores lógicos
"""""

idade = int(input('Digite sua idade: '))
estudante = input('Voce e estudante? (s/n): ').lower() == 's'
tem_cnh = input('Voce possui cnh? (s/n): ').lower() == 's'

if idade < 18 and not tem_cnh:
    print("Você é menor de idade e não possui CNH.")
elif idade < 18 and tem_cnh:
    print("Você é menor de idade, mas possui CNH (Estranho?).")
elif idade >= 18 and estudante and tem_cnh:
    print("Você é maior de idade, estudante e possui CNH.")
elif idade >= 18 and not estudante and tem_cnh:
    print("Você é maior de idade, não é estudante, mas possui CNH.")
else:
    print("Você é maior de idade e não possui CNH.")