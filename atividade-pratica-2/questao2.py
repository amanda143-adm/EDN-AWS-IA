c# Dados do produto
produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# Cálculo do desconto
valor_desconto = (preco_original * percentual_desconto) / 100
preco_final = preco_original - valor_desconto

# Exibindo os resultados
print("Produto:", produto)
print("Preço original: R$", round(preco_original, 2))
print("Desconto:", percentual_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final com desconto: R$", round(preco_final, 2))    




