meta = 2000
cadastro = 'S'

while cadastro == 'S':
    nome = input('qual o nome do vendedor: ')
    valor_venda = float(input('quanto o vendedor vendeu: '))
    atingimento = (valor_venda / meta) * 100
    cadastro = input('deseja sair do cadastro [S/N]: ')


    print(f'nome: {nome}')  
    print(f'valor de venda: {valor_venda}') 
    print(f'atingimento: {atingimento}')
    

