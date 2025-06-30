def classificar_idade(idade):
    if idade >= 0 and idade <= 12:
        return "Você é uma criança."
    elif idade >= 13 and idade <= 17:
        return "Você é um adolescente."
    elif idade >= 18 and idade <= 59:
        return "Você é um adulto."
    elif idade >= 60:
        return "Você é um idoso."
    else:
        return "Idade inválida."

# Entrada do usuário
idade_usuario = int(input("Digite a sua idade: "))
print(classificar_idade(idade_usuario))