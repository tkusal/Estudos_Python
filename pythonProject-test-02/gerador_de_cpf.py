from random import randint

loop = 'S'
soma = 0
ref = 10

while loop == 'S':
    while True:
        cpf = str(randint(100000000, 999999999))
        if cpf == cpf[::-1]:
            continue
        else:
            verif_cpf = cpf
            break

    for i in range(19):
        if i > 8:
            i -= 9

        soma += int(verif_cpf[i]) * ref

        ref -= 1
        if ref < 2:
            ref = 11
            digit = 11 - (soma % 11)

            if digit > 9:
                digit = 0
            soma = 0
            verif_cpf += str(digit)
        
    cpf = '{}.{}.{}-{}'.format(verif_cpf[:3], verif_cpf[3:6], verif_cpf[6:9], verif_cpf[9:])

    print(f'O novo CPF é: {cpf}\n')

    looping = True
    while looping:
        loop = input('Deseja gerar outro CPF? (S/ N)_ ')
        loop = loop.upper()
        looping = False if loop == 'S' or loop == 'N' else True
        if not loop == 'S' or loop == 'N':
            print('Resposta inválida')

print('FIM.')
