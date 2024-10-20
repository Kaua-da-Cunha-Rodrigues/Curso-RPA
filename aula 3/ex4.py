auxiliar = 0
notas = 0
i = 1
for i in range(1, 4):
    nota = float(input(f"Digite a {i}° nota: "))
    notas += nota
    auxiliar += 1

media = notas / 3

if nota < 5:
    print(f"Média: {media}. O aluno está reprovado")
elif nota <= 7:
    print(f"Média: {media}. O aluno está de recuperação")
else:
    print(f"Média: {media}. O aluno está aprovado")