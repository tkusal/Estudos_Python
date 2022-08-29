"""
Repetição com FOR

Função range(start, stop, step)
"""
# Ex.1
texto = 'Oi Mundo'

for n, letra in enumerate(texto):
    print(n, letra)

print()
print()
# Ex.2
for n in range(5):
    print(n)

print()
print()

for n in range(40, 100, 20):
    print(n)
print()
print()
"""
LISTAS
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# indices +     0    1   2   3     4
# novaLista = ['A', 'B', 2, 10.5, 'Carro']
# indices -    -5   -4  -3  -2    -1

l1 = [1, 2, 3]
l2 = [5, 6, 7]

l1.extend(l2)  # adiiona a lista 2 na lista 1
l2.append('b')  # adiciona mais um valor ao final da lista
l1.insert(0, 'INSERT')  # Insere um valor em um indice especifico, reposicionando os pré existentes
l3 = l1 + l2  # concatena as duas listas em uma nova lista
l3.pop()  # remove o último elemento

print(l1)
print(l2)
print(l3)
print()
del(l3[0:2])  # excluir os indices do 0 ao 2 da l3
print(min(l3))  # imprime o menor valor
print(max(l3))  # imprime o maior valor
print()
print()

l1 = list(range(0, 100, 13))  # cria uma lista com números de 0 a 100 em passo de 13 em 13
print(l1)

for valor in l1:
    print(valor * 2)
print()
print()


