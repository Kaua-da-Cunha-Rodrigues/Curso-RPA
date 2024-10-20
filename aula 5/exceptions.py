def tratamentoExcecoes():
    try:
        #Tenta fazer algo, se der algum erro entra nos excepts
        num = int(input("Digite um número: "))
        resultado = 10 / num
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        #Se o valor digitado for zero
        print("Erro: Divisão por zero não é permitida")
    except ValueError:
        #Se o valor digitado não for um número
        print("Erro: O valor digitado não é um número")
    else:
        #Se nenhuma exceção entrar
        print("Código rodado com sucesso!")
    finally:
        #Roda independente de uma exceção ser rodada ou não
        print("Código encerrado!")

tratamentoExcecoes()
