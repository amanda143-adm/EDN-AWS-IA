converte_para_celsius = lambda temperatura, unidade: \
    temperatura if unidade == 'Celsius' else \
    (temperatura - 32) * 5 / 9 if unidade == 'Fahrenheit' else \
    temperatura - 273.15

converte_para_fahrenheit = lambda temperatura, unidade: \
    temperatura if unidade == 'Fahrenheit' else \
    (temperatura * 9 / 5) + 32 if unidade == 'Celsius' else \
    (temperatura - 273.15) * 9 / 5 + 32

converte_para_kelvin = lambda temperatura, unidade: \
    temperatura if unidade == 'Kelvin' else \
    (temperatura + 273.15) if unidade == 'Celsius' else \
    (temperatura - 32) * 5 / 9 + 273.15

def converte_temperatura(temperatura, unidade_origem, unidade_destino):
    if unidade_origem == 'Celsius':
        resultado = converte_para_celsius(temperatura, unidade_destino)
    elif unidade_origem == 'Fahrenheit':
        resultado = converte_para_fahrenheit(temperatura, unidade_destino)
    elif unidade_origem == 'Kelvin':
        resultado = converte_para_kelvin(temperatura, unidade_destino)
    else:
        print("Unidade de origem inválida.")
        return

    print(f"{temperatura}° {unidade_origem} equivale a {resultado:.2f}° {unidade_destino}")

converte_temperatura(100, 'Celsius', 'Fahrenheit')
converte_temperatura(32, 'Fahrenheit', 'Celsius')
converte_temperatura(273.15, 'Kelvin', 'Celsius')