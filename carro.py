preco1 = float(input('Digite o preço do carro no 1º ano:'))
preco2 = float(input('Digite o preço do carro no 2º ano:'))
preco3 = float(input('Digite o preço do carro no 3º ano:'))

maior_preco = max(preco1, preco2, preco3)
menor_preco = min(preco1,preco2,preco3)

if maior_preco==preco1:
    print(f'O carro mais caro é do 1º ano e custa {maior_preco}')
elif maior_preco==preco2:
    print(f'O carro mais caro é do 2º ano e custa {maior_preco}')
else: 
    print(f'O carro mais caro é do 3º ano e custa {maior_preco}')

if menor_preco==preco1:
    print(f'O carro mais barato é do 1º ano e custa {menor_preco}')
elif menor_preco==preco2:
    print(f'O carro mais barato é do 2º ano e custa {menor_preco}')
else: 
    print(f'O carro mais barato é do 3º ano e custa {menor_preco}')


