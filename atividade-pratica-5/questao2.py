def verifica_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    
    return palavra == palavra[::-1]

input_palavra = input("Digite uma palavra ou frase: ")
if verifica_palindromo(input_palavra):
    print(f'"{input_palavra}" é um palíndromo.')
else:
    print(f'"{input_palavra}" não é um palíndromo.')