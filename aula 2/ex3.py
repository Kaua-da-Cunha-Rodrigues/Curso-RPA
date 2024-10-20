def calcular():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    operador = input("Digite o tipo do cálculo (soma, subtração, multiplicação ou divisão): ")

    if operador == "soma":
        resultado = valor1 + valor2
    elif operador == "subtração":
        resultado = valor1 - valor2
    elif operador == "divisão":
        resultado = valor1 / valor2
    elif operador == "multiplicação":
        resultado = valor1 * valor2

    print(f"O resultado é: {resultado}")

calcular()