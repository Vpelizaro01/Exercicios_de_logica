nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nomes_formatados = [nome.capitalize() for nome in nomes]
sobrenomes_formatados = [sobrenomes.capitalize()for sobrenomes in sobrenomes]

for i in range(len(nomes)):
    nome_completo = f"{nomes_formatados [i]} {sobrenomes_formatados[i]}"
    print(nome_completo)
