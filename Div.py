
numero1 = int(input('Digite um numero: '))
denominador = int(input('Digite outro numero: '))
 
if denominador == 0:
    print(f"Não se divide 0")
    
else:
 resultado = numero1 % denominador
 print(f"Resultado é {resultado}")