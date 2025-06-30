def calcular_massa_corporal(peso, altura):
    imc = peso / (altura ** 2)  
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc and imc < 25:
        return "Peso normal"
    elif 25 <= imc and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
print(calcular_massa_corporal(70, 1.75))