notas = []

for i in range(4):
    nota = float(input(f"Digite a sua nota {i+1} /4: "))
    notas.append(nota)

nota_maxima = max(notas)
nota_minima = min(notas)
media_notas = sum(notas)/len(notas)


if media_notas >= 5:
    situacao = "Aprovado"   
else:
   situacao = "Reprovado"


print(f"O(a) estudante obteve uma média de {nota_maxima}, com a sua maior nota de {nota_minima} pontos e a menor nota de  {media_notas:.2f} pontos e foi  {situacao} ")