def calculadora():
    try:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro! Divisão por zero não é possível")
    except ValueError:
        print("Erro! Um dos valores digitados não é um número")
    else:
        print("Cálculo realizado com sucesso!")
    finally:
        print("Código terminou de rodar")

calculadora()