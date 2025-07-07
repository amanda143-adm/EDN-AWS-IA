def calcula_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

notas = []
while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

media = calcula_media(notas)
print(f"A média das notas é: {media:.2f}")