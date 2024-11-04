resultados = [
    ("Equipe A", [10, 8, 9]),
    ("Equipe B", [7, 8, 8]),
    ("Equipe C", [9, 9, 10])
]
medias = [(equipe, sum(pontos) / len(pontos)) for equipe, pontos in resultados]
medias.sort(key=lambda x: x[1], reverse=True)
classificacao = [(equipe, media) for equipe, media in medias]
print("Classificação Final:")
for equipe, media in classificacao:
    print(f"{equipe}: média de {media:.2f}")