def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = calcular_media(nota1, nota2, nota3)

media_arredondada = round(media, 2)
print("A média é:", media)
print("A média arredondada é:", media_arredondada)
