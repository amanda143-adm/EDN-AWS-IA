def conversor_de_moeda():
    valor_em__reais = 100.00
    taxa_do_dolar = 5.20
    taxa_do_euro = 6.15
    valor_em_dolares = valor_em__reais / taxa_do_dolar
    valor_em_euros = valor_em__reais / taxa_do_euro
    print(f"Valor em reais: R$ {valor_em__reais:.2f}")
    print(f"Valor em dólares: $ {valor_em_dolares:.2f}")
    print(f"Valor em euros: € {valor_em_euros:.2f}")
conversor_de_moeda()
# Output:
# Valor em reais: R$ 100.00
# Valor em dólares: $ 19.23
# Valor em euros: € 16.26
# A função converte um valor em reais para dólares e euros, exibindo os resultados formatados.
# A função calcula o valor em dólares e euros dividindo o valor em reais pelas respectivas taxas de câmbio.
# O resultado é impresso com duas casas decimais para cada moeda.
    
    
    


