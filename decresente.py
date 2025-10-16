num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))
num3 = int(input('Digite mais um numero:'))

if num1 < num2 < num3:
    print(f'Os numeros em ordem decrescente são: {num3} , {num2} , {num1}')
elif num1 < num3 < num2:
    print(f'Os numeros em ordem decrescente são: {num2} , {num3} , {num1}')
else:
    print(f'Os numeros em ordem decrescente são: {num1} , {num2} , {num3}')