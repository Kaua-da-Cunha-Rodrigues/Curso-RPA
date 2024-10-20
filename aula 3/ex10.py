inteiro = int(input("Digite um valor para cálculo de fatorial: "))
fatorial = 1
for i in range(1, inteiro + 1):
    fatorial *= i

print(f"O fatorial de {inteiro} é: {fatorial}")