notas_skate = []

for i in range(5):
    nota = float(input(f"Digite a nota do skatista:  "))
    notas_skate.append(nota)

notas_skate.remove(max(notas_skate))
notas_skate.remove(min(notas_skate))

media = sum (notas_skate)/len(notas_skate)
print(f"A média das notas é: {media:.2f}")

