nome = "Kauã"
sobrenome = " da Cunha Rodrigues"
nome_completo = nome + sobrenome
idade = 11
altura = 1.75
alunoRPA = True


def exibirInfos(nome, idade, altura):
    print(f"Olá {nome}!")
    print(f"Suas informações: \nIdade: {idade} \nAltura: {altura}")
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")

def verificarTipo(variavel):
    print(f"O tipo da variável é: {type(variavel)}")

exibirInfos(nome_completo, idade, altura)
