lado1 = float(input('Digite o valor do primeiro lado do triângulo:'))
lado2 = float(input('Digite o valor do segundo lado do triângulo:'))
lado3 = float(input('Digite o valor do terceiro lado do triângulo:'))


if (lado1 < lado2 + lado3) and ( lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
        print(f'Os lados formam um triângulo')
elif lado1 == lado2 == lado3:
        print(' O triângulo é equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triângulo é isósceles')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('O triângulo é escaleno')
else:
    print('Os lados não formam um triângulo')
