def calcula_gorgeta(valor_total, porcentagem):
    return valor_total * (porcentagem / 100)

print("=== Calculadora de Gorjeta ===")

try:
    porcentagem_garcom = float(input("Digite a porcentagem da gorjeta (ex: 10, 12.5): "))
    valor_total_cliente = float(input("Digite o valor total da conta: R$ "))

    gorjeta = calcula_gorgeta(valor_total_cliente, porcentagem_garcom)
    total_com_gorgeta = valor_total_cliente + gorjeta

    print("\n=== Resultado ===")
    print(f"Gorjeta ({porcentagem_garcom:.1f}%): R$ {gorjeta:.2f}")
    print(f"Total a pagar (com gorjeta): R$ {total_com_gorgeta:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite números válidos.")
