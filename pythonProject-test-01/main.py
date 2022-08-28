# Aplicando primeiros conceitos

# Print com separador e END. Ex.: Separador de CPF

"""
Por padrão a função print pula um linha.
O end permite esecutar a próxima função na mesma linha e/ou colocando algo como separador
sep define um separador entre os textos
"""

print('CPF: ', end='')
print('888', '555', '333', sep='.', end='-')
print('15')

#  A saída acima foi "CPF: 888.555.333-15"
#  Texto abaixo com quebra de linha

print("\n Este 'texto' possui \n uma quebra de linha\n")

"""
Tipos de dados:

str (String) - texto entre aspas simples ou duplas
int (Inteiro) - números inteiros, positivos ou negativos
float (real/flutuante) - números reais. Casas decimais separadas por ponto
bool (booleano) - True ou False  Ex.: 10 == 10
"""

print(type('palavra'))  #str
print(type(10))  #int
print(type(10.10))  #float
print(type(10 >= 10), '\n')  #bool

# Ex,: alterando uma string para inteiro
print('300', type('300'))
print(int('300'), type(int('300')), '\n')

"""
Operadores lógicos:
+   Adição ou Concatenação de Strings
-   Subtração
*   Multiplicação ou repetição de string
/   Divisão
//  Divisão inteira
**  exponenciação
%   módulo: resto da divisão

Precedência aritmética: (), **,  [* / // %], [+ -]
"""

print(30+10)
print(30-10)
print(30*10)
print(30/10)
print(30//11)
print(2**4)
print(30%11, '\n')
print('Multiplcação usada para repetição de uma string:\n', 5 * ('String repetida 5x\n'))

"""
Variáveis:
Sempre iniciar com letras, pode conter números e separar com _ e utilizar letras minúsculas.
"""

nome = 'Fulano'
idade = 40
altura = 1.77
maioridade = idade >= 18
peso = 80
imc = peso / (altura **2)

print('O nome é', nome + ', possui', idade, 'anos, e tem', altura, 'm de altura. Ele é maior de idade?', maioridade)
print('Seu imc é de', imc, '\n\n')
# melhor forma de exibição, utilizando F-Strong
print(f'Seu nome é {nome}, possui {idade} anos, pesa {peso}kg e tem {altura}m de altura.\nSeu IMC é de {imc:.2f}')
# Outra forma de concatenar as variáveis com o texto do print, utilizando F-String
print('Seu nome é {0}, possui {1} anos e pesa {2}kg e seu IMC é de {3:.2f} - {0} {1} {2} {3}\n\n'.format(nome, idade, peso, imc))

# Fazer input

nome = input('Digite seu nome:\n')
# idade = int(input('Digite sua idade:\n'))
# nasc = 2022-idade
# print(f'{nome} tem {idade} anos e nasceu em {nasc}\n')

"""
Condicionais: IF, ELIF, ELSE
Operadores: == > >= < <= != 
           and, or, not
           in, not in
"""

num = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))
print()


if num == num2:
    print('Os numeros são iguais')
elif num > num2:
    print('O primeiro numero é maior')
elif num < num2:
    print('O segundo numero é maior')
else:
    print('Que porra é essa?')

print()

"""
Verificar quantos caracteres há dentro de uma string
"""

qtd_caracteres = len(nome)
print(qtd_caracteres)