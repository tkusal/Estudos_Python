"""
Manipulação de Strings
"""

# Indices de string
var = 'String Py'
# Positivos   [012345678]
# var       = 'String Py'
# Negativos  -[987654321]

print(var[0])
novaString = var[6:8]
print(novaString)
novaString = var[5:]
print(novaString)
novaString = var[-9]
print(novaString)
print()

# While
# continue, dentro do bloco while, pula a execução para o próximo passo.
# No exemplo abaixo, ele irá exibir os números de 0 a 10, porém irá pular o número 5

x = 0
while x <= 10:
    if x == 5:
        x = x + 1
        print('XXX')
        continue
    print(x)
    x = x + 1

# break, dentro do bloco while, encerra o laõ
# No exemplo abaixo, ele irá exibir os números de 0 a 10, porém irá encerrar o laço no número 5

x = 0
while x <= 10:
    if x == 5:
        x += 1
        print('XXX')
        break
    print(x)
    x += 1
print('Encerrado')
print()

# while - Teste de matriz

x = 0
while x <= 5:
    y = 0
    while y <= 5:
        print(f'Valor de X:y - {x}:{y}')
        y += 1
    x += 1

print('Fim\n')
print()

# Tabuada

while True:
    x = 1
    while True:
        num = input('Digite um valor inteiro para retornar a tabuada:\n')
        if num.isnumeric():
            num = int(num)
            break
        else:
            print("Digite um valor válido")

    op = input('Digite a opção desejada:\n1- Multiplicação\n2-Divisão\n3-Soma\n4-Subtração\n5- Fim\n')
    if op == '1':
        while x <= 10:
            result = num * x
            print(f'{num} x {x} = {result}')
            x += 1
    elif op == '2':
        while x <= 10:
            result = num / x
            print(f'{num} / {x} = {result:.2f}')
            x += 1
    elif op == '3':
        while x <= 10:
            result = num + x
            print(f'{num} + {x} = {result}')
            x += 1
    elif op == '4':
        while x <= 10:
            result = num + x
            print(f'{num} + {x} = {result}')
            x += 1
    elif op == '5':
        break

print('FIM\n')
print()

# Iteração

frase = input('Digite uma frase:\n')
input = input('Digite a letra que quer deixar em maiúscula: ')
input = input.lower()
frase = frase.lower()
contador = 0
novaString = ' '
tamanho = len(frase)

while contador < tamanho:
    if frase[contador] == input:
        novaString += input.upper()
    else:
        novaString += frase[contador]
    contador += 1

print(novaString)
print()