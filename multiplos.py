multiplos = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = []

for multiplos in multiplos:
    if multiplos % 3 == 0:
        mult_3.append(multiplos)
print (f"Múltiplos de 3:{mult_3}", )
