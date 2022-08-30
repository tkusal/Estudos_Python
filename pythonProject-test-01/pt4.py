"""
Split, Join, Enumerate
- split: Dividir uma str
- join: juntar uma lista
- enumerate: enumerar os elementos da lista
"""

string1 = "água mole em pedra dura, tanto bate até que fura"
list = string1.split(',')

for valor in list:
    print(valor.strip().capitalize())
print()
print()

string2 = "João vende camisa onde Maria vende bota e é irmã de João"
list2 = string2.split(' ')

for palavra in list2:
    print(f'Palavra: {palavra} | {list2.count(palavra)}x vezes')

print()
print()

# Join

string3 = '-----'.join(list2)
print(list2)
print(string3)
print()
print()

list3 = ['João', 'é', 'brasileiro']

# Enumerate

for indice, valor in enumerate(list3):
    print(indice, valor)
print()
print()

# Desepacotamento de lista

n1, n2, n3 = list3

print(n1)
print(n2)
print(n3)
print()
print()


# Inversão de variáveis
x = 10
y = 'Jão'
x, y = y, x
print(f'{x}, {y}\n\n')

"""
OPERADOR TERNÁRIO
"""
db_user = 'admin'
login_inserido = input('Informe seu login: ')
logged_user = (db_user == login_inserido)
msg = 'Usuário Logado' if logged_user else 'Login incorreto'

print(f'{msg}\n\n')

"""
Codicional com OR
"""

nome = input ('Informe seu nome: ')
print(nome or 'Você não informou seu nome')