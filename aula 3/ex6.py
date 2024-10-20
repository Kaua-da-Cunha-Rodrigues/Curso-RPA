ano = int(input("Digite o ano: "))

if ano % 4 == 0 and not ano % 100 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")