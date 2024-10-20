def solicitarInfos():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    tamanhoNome = len(nome)
    print(f"Olá, {nome}! \nVocê tem {idade} ano(s) \nSeu nome tem {tamanhoNome} caracteres")

solicitarInfos()