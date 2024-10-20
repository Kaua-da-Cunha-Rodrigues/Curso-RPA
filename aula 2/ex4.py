def converterTemperatura(temperatura):
    temperaturaConvertida = 1.8 * temperatura + 32
    print(f"A temperatura em Fahrenheit é: {temperaturaConvertida:.2f}")

temperatura = float(input("Digite a temperatura em Celsius: "))
converterTemperatura(temperatura)