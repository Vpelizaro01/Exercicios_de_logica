vogal = ['a', 'e', 'i', 'o' , 'u']
consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

letra = str(input('Digite uma letra:'))

if letra in vogal:
    print (f'A letra {letra} é uma vogal')
elif letra in consoante: 
    print (f'A letra {letra} é uma consoante')
