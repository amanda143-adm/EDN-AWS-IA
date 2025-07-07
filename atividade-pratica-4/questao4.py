def classificador_numeros_pares_impares(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return (pares, impares)

entrada = input("Digite números inteiros separados por vírgula (ex: 2, 5, 8, 13): ")

try:
    numeros = [int(num.strip()) for num in entrada.split(',') if num.strip() != '']

    pares, impares = classificador_numeros_pares_impares(numeros)

    print("\nClassificação dos números:")
    print(f"Números pares: {sorted(pares)}")
    print(f"Números ímpares: {sorted(impares)}")
    print("=" * 40)
    print(f"Total de números pares: {len(pares)}")
    print(f"Total de números ímpares: {len(impares)}")

except ValueError:
    print("Erro: Certifique-se de digitar apenas números inteiros separados por vírgula.")
