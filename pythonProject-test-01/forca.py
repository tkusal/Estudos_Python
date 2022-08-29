palavraSecreta = 'cAchorro'
digitadas = []
chances = 5

palavraSecreta = palavraSecreta.lower()

print('Bem vindo ao Jogo da forca.')
print('Você pode errar apenas 5 vezes')

while True:
    if chances == 0:
        print('Suas chances acabaram. Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas 1 letra.\n')
        continue
    else:
        letra = letra.lower()

    digitadas.append(letra)

    if letra in palavraSecreta:
        print(f'Parabéns, a letra "{letra}" exsite na palavra secreta')
    else:
        chances -= 1
        print(f'A letra "{letra}" não faz parte da palavra secreta')
        print(f'Você ainda tem {chances} chances')
        digitadas.pop()

    resposta = ''
    for letraSecreta in palavraSecreta:
        if letraSecreta in digitadas:
            resposta += letraSecreta
        else:
            resposta += '*'

    if resposta == palavraSecreta:
        print('Parabéns!!! Você acertou a palavra.')
        break
    else:
        print(f'Sua resposta está assim até agora: {resposta}\n\n')
