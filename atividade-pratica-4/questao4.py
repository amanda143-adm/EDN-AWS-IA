def classificador_numeros_pares_impares(lista):
    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return (pares, impares)

classificacao = input("Digite uma lista de números separados por vírgula: ")
numeros = [int(num.strip()) for num in classificacao.split(',')]

classificacao = classificador_numeros_pares_impares(numeros)
print("Classificação dos números:")
print(f"Números pares: {classificacao[0]}")
print(f"Números ímpares: {classificacao[1]}")