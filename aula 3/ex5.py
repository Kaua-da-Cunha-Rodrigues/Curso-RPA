def calcularIMC(peso, altura):
    imc = peso / altura**2

    if imc < 18.5:
        print(f"Classificação: Magreza \nObesidade (Grau): 0 \nIMC: {imc:.2f}")
    elif imc >= 18.5 and imc < 24.9:
        print(f"Classificação: Normal \nObesidade (Grau): 0 \nIMC: {imc:.2f}")
    elif imc >= 25 and imc <29.9:
        print(f"Classificação: Sobrepeso \nObesidade (Grau): I \nIMC: {imc:.2f}")
    elif imc >= 30 and imc < 39.9:
        print(f"Classificação: Obesidade \nObesidade (Grau): II \nIMC: {imc:.2f}")
    else:
        print(f"Classificação: Obesidade Grave \nObesidade (Grau): III \nIMC: {imc:.2f}")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
calcularIMC(peso, altura)