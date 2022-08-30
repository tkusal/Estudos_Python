loop = 'S'
soma = 0
ref = 10

while loop == 'S':
    while True:
        cpf = input('Informe um CPF(apenas números): ')
        if len(cpf) != 11 or cpf == cpf[::-1]:
            print('Número de CPF Inválido\n\n')
        else:
            print('Validando CPF...\n\n')
            verif_cpf = cpf[:-2]
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

    msg = ('CPF Válido' if cpf == verif_cpf else 'CPF Inválido')
    print(f'{msg}\n')

    looping = True
    while looping:
        loop = input('Deseja testar outro CPD? (S/ N)_ ')
        loop = loop.upper()
        looping = False if loop == 'S' or loop == 'N' else True
        if not loop == 'S' or loop == 'N':
            print('Resposta inválida')

print('FIM.')
