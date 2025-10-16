porcentual_positivo = float(input('Digite o valor do porcentual da sua empresa:'))


if porcentual_positivo > 0:
    print('Sua empresa é lucrativa')
elif porcentual_positivo < 0:
    print ('Sua empresa está em prejuizo')
else:
    print('Sua empresa está em equilíbrio')