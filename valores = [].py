# Programa 4
caracteres = []
consoantes = []
vogais = {'a', 'e', 'i', 'o', 'u'}

for i in range(10):
    char = input(f"Digite o {i+1}º caractere: ").lower()
    if char.isalpha():
        caracteres.append(char)
        if char not in vogais:
            consoantes.append(char)

print("Consoantes lidas:", consoantes)
print("Quantidade de consoantes:", len(consoantes))
