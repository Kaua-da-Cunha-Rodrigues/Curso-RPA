def juntarNome(nome, sobrenome):
    nomeCompleto = nome + " " + sobrenome
    print(f"Seu nome completo é: {nomeCompleto}")

nome = input("Digite o primeiro nome: ")
sobrenome = input("Digite seu segundo nome: ")
juntarNome(nome, sobrenome)