# Realizar a soma de dois números inteiros e verificar se o resultado é par ou ímpar
# Certificar que o usuário não dará input com um caracter que não seja númerico
correto = False

while correto != True:

    num1 = input('Digite o primeiro número inteiro: ')
    num2 = input('Digite o segundo Número inteiro: ')
    print()

    if num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
        soma = num1 + num2
        correto = True
        if soma % 2 == 0:
            print(f'A soma de dos dois número é {soma} e é um número par.')
        else:
            print(f'A soma dos dois números é {soma} e é um número ímpar')
    else:
        if not num1.isnumeric():
            print('O primeiro valor informado não é um número inteiro')
        elif not num2.isnumeric():
            print('O segundo valor informado não é um número inteiro')