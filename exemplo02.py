resposta = 's'
while resposta == 's':
    numero = int(input('informe um numero: '))

    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f'dobro: {dobro}')
    print(f'triplo: {triplo}')
    print(f'quadrado: {quadrado}')

    resposta = input('quer continuar: [s/n]').upper()
