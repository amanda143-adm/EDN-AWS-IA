def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

def calculadora(x, y, operacao):
    if operacao == '1':
        return soma(x, y)
    elif operacao == '2':
        return subtracao(x, y)
    elif operacao == '3':
        return multiplicacao(x, y)
    elif operacao == '4':
        return divisao(x, y)
    elif operacao == '5':
        return "Saindo da calculadora"
    else:
        return "Operação inválida"

def main():
    while True:
        try:
            x = int(input("Digite o valor de X: "))
            y = int(input("Digite o valor de Y: "))
            break
        except ValueError:
            print("Valor inválido. Digite números inteiros.")
    while True:
        print("Escolha a operação desejada:")
        print("1: Adição")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("5: Sair")
        operacao = input("Digite o número da operação desejada: ")
        if operacao == '5':
            print("Saindo da calculadora")
            break
        try:
            resultado = calculadora(x, y, operacao)
            if resultado == "Operação inválida":
                print("Operação inválida, tente novamente.")
                continue
            print("O resultado é:", resultado)
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

main()