gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(gols_marcados, gols_sofridos):
 pontos = 0
 for i in range(len(gols_marcados)):
  if gols_marcados[i] > gols_sofridos[i]:
   pontos += 3
  elif gols_marcados[i] <  gols_sofridos[i]:
   pontos += 0
 else:
    pontos += 1
 aproveitamentos = sum(gols_marcados)/sum(gols_sofridos)*100
 return pontos, aproveitamentos

pontos,aproveitamentos = calcula_pontos(gols_marcados, gols_sofridos)

print(f"O time fez {pontos} pontos na temporada e seu aproveitamento foi de {aproveitamentos:.2f}%")
     



