def calcula_valor_com_desconto(valor_total, porcentagem_desconto):
    return valor_total * (1 - porcentagem_desconto / 100)

print("=== Calculadora de Desconto ===")

try:
    porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 10, 15.5): "))
    valor_total_cliente = float(input("Digite o valor total da compra: R$ "))

    valor_com_desconto = calcula_valor_com_desconto(valor_total_cliente, porcentagem_desconto)

    print("\n=== Resultado ===")
    print(f"Valor com desconto ({porcentagem_desconto:.1f}%): R$ {valor_com_desconto:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite números válidos.")