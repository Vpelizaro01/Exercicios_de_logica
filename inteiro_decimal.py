numero = input('Digite um numero: ')

try:
    valor = float (numero)
    if valor == int(valor):
        print(f"O numero {numero} é inteiro")
    else:
        print(f"O numero {numero} é decimal")
except ValueError:
    print("Entrada inválida. Tente Novamente.")


