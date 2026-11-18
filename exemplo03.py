while True:

    numero = int(input('informe um numero: '))

    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2
 
    print(f'dobro: {dobro}')
    print(f'triplo: {triplo}')
    print(f'quadrado: {quadrado}')
 
    resposta = input('quer continuar: [S/N]').upper()   
    
    if resposta == 'N':
            break
    