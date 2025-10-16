numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominado: "))

if denominador ==0:
    print("error")
else:
    resultado = numerador / denominador
    print(f'O resultado da divisão é {resultado}')
