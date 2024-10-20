def abrirArquivo(nome):
    try:
        if ".txt" not in nome:
            nome += ".txt"
        arquivo = open(nome, "r")
        print(arquivo.read())
    except FileNotFoundError:
        print(f"Erro! o arquivo {nome} não foi encontrado")
    else:
        arquivo.close()
        print("Arquivo lido com sucesso!")
    finally:
        print("Código rodado!")

nome = input("Digite o nome do arquivo: ")
abrirArquivo(nome)
