num1 = float(input('Digite o primeiro número: '))
num2  = float(input('Digite o segundo número: '))
operacao = input ('Digite a operação desejada (+, - , * , /)')

if operacao == '+':
    resultado = num1 + num2
    print(f'O resultado da soma é {resultado}')
elif operacao == '-':
    resultado = num1 - num2 
    print (f'O resuldado da subtração é {resultado}')
elif operacao == '*':
    resultado = num1 * num2
    print (f'O resultado da multiplicação é {resultado}')
elif operacao == '/':
    if num2 == 0:
        print('Não se divide por 0')
    else:
        resultado = num1/num2
        print (f"primeiro número divido pelo segundo é {resultado}")
