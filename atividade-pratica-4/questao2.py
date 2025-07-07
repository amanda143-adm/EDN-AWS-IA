def calcula_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

notas = []

print("=== Calculadora de Média ===")
print("Digite suas notas de 0 a 10.")
print("Digite 'fim' para encerrar.\n")

while True:
    entrada = input("Informe uma nota (ou 'fim'): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
            print(f"Nota {nota:.1f} adicionada com sucesso.")
        else:
            print("Nota inválida. Deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

print("\n=== Resultado ===")
if notas:
    media = calcula_media(notas)
    print(f"Notas digitadas: {', '.join(f'{n:.1f}' for n in notas)}")
    print(f"Total de notas: {len(notas)}")
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
