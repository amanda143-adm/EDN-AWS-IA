from datetime import datetime

def calcular_dias_vividos(ano_nascimento, mes_nascimento, dia_nascimento):
    data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
    data_atual = datetime.now()
    dias_vividos = (data_atual - data_nascimento).days
    return dias_vividos, data_nascimento

print("=== Calculadora de Dias Vividos ===")

try:
    input_ano = int(input("Digite o ano de nascimento (ex: 1995): "))
    input_mes = int(input("Digite o mês de nascimento (1-12): "))
    input_dia = int(input("Digite o dia de nascimento (1-31): "))

    dias_vividos, data_nasc = calcular_dias_vividos(input_ano, input_mes, input_dia)

    print("\n=== Resultado ===")
    print(f"Data de nascimento: {data_nasc.strftime('%d/%m/%Y')}")
    print(f"Você viveu aproximadamente {dias_vividos:,} dias.".replace(',', '.'))

except ValueError:
    print("\nData inválida. Certifique-se de digitar valores corretos para dia, mês e ano.")
